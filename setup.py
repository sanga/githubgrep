import versioneer

from setuptools import setup

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
    entry_points={
        'console_scripts': [
            'ghgrep = githubgrep.grep:run',
        ],
    },
    zip_safe=False)
