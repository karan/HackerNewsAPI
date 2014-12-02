import unittest

from hn import HN, Story
from hn import utils, constants

from test_utils import get_content, PRESETS_DIR

import httpretty


class TestGetLeaders(unittest.TestCase):
    def setUp(self):
        # check py version
        # #self.PY2 = sys.version_info[0] == 2
        self.hn = HN()
        httpretty.HTTPretty.enable()
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
                                                         'leaders'),
                               body=get_content('leaders.html'))

        def tearDown(self):
            httpretty.HTTPretty.disable()

        def test_get_leaders_with_no_parameter(self):
            result = [leader for leader in self.hn.get_leaders()]
            self.assertEqual(len(result), 10)

        def test_get_leaders_with_parameter(self):
            value = 50
            result = [leader for leader in self.hn.get_leaders(value)]
            self.assertEqual(len(result), value)


if __name__ == '__main__':
    unittest.main()
