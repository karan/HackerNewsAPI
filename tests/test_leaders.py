import unittest
import sys
import os

from hn import HN, Story
from hn import utils

if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from tests.cases import RemoteTestCase
    unicode = str
else:
    from urllib2 import urlopen
    from cases import RemoteTestCase

class TestGetLeaders(RemoteTestCase):

	def setUp(self):
		# check py version
		#self.PY2 = sys.version_info[0] == 2
		self.hn = HN()

	def tearDown(self):
		pass

	def test_get_leaders_with_no_parameter(self):
		result = [leader for leader in self.hn.get_leaders()]
		self.assertEqual(len(result), 10)

	def test_get_leaders_with_parameter(self):
		value = 50
		result = [leader for leader in self.hn.get_leaders(value)]
		self.assertEqual(len(result), value)


if __name__ == '__main__':
    unittest.main()
