try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='HackerNews',
    version='1.3.2',
    install_requires=['BeautifulSoup4>=4.3.1',],
    author='Karan Goel',
    author_email='karan@goel.im',
    packages=['hn',],
    url='https://github.com/thekarangoel/HackerNewsAPI/',
    license='GNU General Public License',
    description='Python API for Hacker News.',
    long_description=open('README.rst').read(),
)
