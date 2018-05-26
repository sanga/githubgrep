import versioneer

from setuptools import setup
from pip.req import parse_requirements


def get_requirements(filename='requirements.txt'):
    # note this is using an internal, unstable pip API
    # but it's hasn't broken in years and is better
    # than writing the same thing by hand
    reqs = parse_requirements(filename, session='dummy')
    return [str(req.req) for req in reqs]


setup(
    name='githubgrep',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='',
    url='http://github.com/sanga/githubgrep',
    author='Tim Sampson',
    author_email='tim@sampson.fi',
    license='MIT',
    packages=['githubgrep'],
    install_requires=get_requirements(),
    zip_safe=False
)
