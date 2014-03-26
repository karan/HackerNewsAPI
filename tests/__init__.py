import sys
import os

import unittest

if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from tests.cases import RemoteTestCase
    unicode = str
else:
    from urllib2 import urlopen
    from cases import RemoteTestCase


def load_tests(loader, tests, discovery):
    for attr, envvar in [('_do_local', 'LOCAL'), ('_do_remote', 'REMOTE')]:
        envvar = os.environ.get(envvar)
        if envvar is not None:
            setattr(RemoteTestCase, attr, envvar.lower() in ['true', '1'])
    return unittest.TestSuite(tests)
