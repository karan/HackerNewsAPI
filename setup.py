try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='HackerNews',
    version='1.4.4',
    install_requires=['BeautifulSoup4>=4.3.1',],
    author='Karan Goel',
    author_email='karan@goel.im',
    packages=['hn',],
    url='https://github.com/thekarangoel/HackerNewsAPI/',
    license='GNU General Public License',
    description='Python API for Hacker News.',
    long_description='Unofficial Python API for Hacker News. Usage: https://github.com/thekarangoel/HackerNewsAPI.',
)
