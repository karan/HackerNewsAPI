import unittest
import sys

from testscenarios import TestWithScenarios


if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from urllib.error import URLError
    from tests.server import hn
else:
    from urllib2 import urlopen, URLError
    from server import hn


class RemoteTestCase(TestWithScenarios):
    _do_local = True
    _do_remote = False

    @classmethod
    def setUpClass(cls):
        """
        Start local server and setup local and remote urls defaulting to local
        one.
        """
        cls.server = hn
        cls.server.start()
        cls.remote = 'https://news.ycombinator.com'
        cls.local = cls.server.url
        cls.scenarios = []
        if cls._do_local:
            cls.scenarios.append(('local', {'url': cls.local}))
        if cls._do_remote and cls._is_remote_available:
            cls.scenarios.append(('remote', {'url': cls.remote}))

    @classmethod
    def tearDownClass(cls):
        """
        Stop local server.
        """
        cls.server.stop()

    @property
    @classmethod
    def _is_remote_available(cls):
        """
        Check connectivity to remote.
        """
        try:
            urlopen(cls.remote)
        except URLError:
            return False
        else:
            return True

    def _assertCountEqual(self, first, second):
        """
        Compatibility function to test if the first sequence contains the
        same elements as the second one.

        This was done in order to have backwards compatibility between python
        2.x and 3.x
        """
        if sys.version_info >= (3, 0):
            self.assertCountEqual(first, second)
        else:
            self.assertItemsEqual(first, second)
