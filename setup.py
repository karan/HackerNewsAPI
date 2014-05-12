try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '2.0.0'

setup(
    name='HackerNews',
    version=version,
    install_requires=['BeautifulSoup4>=4.3.1', 'requests'],
    author='Karan Goel',
    author_email='karan@goel.im',
    packages=['hn', 'tests'],
    test_suite='tests',
    url='https://github.com/karan/HackerNewsAPI/',
    license='MIT License',
    description='Python API for Hacker News.',
    long_description='Unofficial Python API for Hacker News. Usage: https://github.com/karan/HackerNewsAPI.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
