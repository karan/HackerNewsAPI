try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='HackerNews',
    version='1.6.2',
    install_requires=['BeautifulSoup4>=4.3.1', 'requests'],
    author='Karan Goel',
    author_email='karan@goel.im',
    packages=['hn', 'tests'],
    test_suite='tests',
    url='https://github.com/karan/HackerNewsAPI/',
    license='MIT License',
    description='Python API for Hacker News.',
    long_description='Unofficial Python API for Hacker News. Usage: https://github.com/karan/HackerNewsAPI.',
)
