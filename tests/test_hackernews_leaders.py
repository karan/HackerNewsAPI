import unittest
import sys

from hn import HN, Story
from hn import utils

class TestGetHackerNewsLeaders(unittest.TestCase):
	def setUp(self):
		# check py version
		self.PY2 = sys.version_info[0] == 2
		self.hn = HN()

	def tearDown(self):
		pass

	def test_get_hackernews_leaders_with_no_parameter(self):
		result = [leader for leader in self.hn.get_hackernews_leaders()]
		self.assertEqual(len(result), 10)

	def test_get_hackernews_leaders_with_parameter(self):
		value = 50
		result = [leader for leader in self.hn.get_hackernews_leaders(value)]
		self.assertEqual(len(result), value)

if __name__ == '__main__':
    unittest.main()