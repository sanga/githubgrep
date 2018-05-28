import logging
import os
import re
import sys

from requests_toolbelt.sessions import BaseUrlSession

LOGGER = logging.getLogger(__name__)


class Session(BaseUrlSession):
    def __init__(self,
                 url='https://api.github.com',
                 include_text_matches=False):
        super().__init__(url)
        self.headers = {'User-Agent': 'githubgrep-python-client'}
        if include_text_matches:
            self.headers[
                'Accept'] = 'application/vnd.github.v3.text-match+json',


class Client:
    def __init__(self, username=None, password=None):
        username = username or os.getenv('GITHUB_USERNAME')
        password = password or os.getenv('GITHUB_AUTH_TOKEN')
        self._sess = Session()
        self._sess.auth = (
            username,
            password,
        )

    def _search(self, q):
        LOGGER.info('searching with query: %s', q)
        return self._sess.get('search/code', params={'q': q})

    def search(self, q, limit=5):
        resp = self._search(q)
        resp.raise_for_status()
        j = resp.json()
        h = []
        for i in j['items']:
            if len(h) <= limit:
                h.append(i['html_url'])
        return [self._get_raw_link(g) for g in h]

    @staticmethod
    def _get_raw_link(url):
        return re.sub('^https://github.com(.*)blob/(.*)',
                      'https://raw.githubusercontent.com\g<1>\g<2>', url)


def run():
    c = Client()
    res = c.search(sys.argv[1])
    for i in res:
        print(i)
