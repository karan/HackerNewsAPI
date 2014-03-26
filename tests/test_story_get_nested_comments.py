import sys
import os

from hn import Story
import unittest

if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from tests.cases import RemoteTestCase
    unicode = str
else:
    from urllib2 import urlopen
    from cases import RemoteTestCase

class TestStoryGetComments(RemoteTestCase):

    def setUp(self):
        self.story = Story.fromid(7404389)
        self.comments = self.story.get_comments()

    def test_get_nested_comments(self):
    	comment = self.comments[0].body
    	self.assertTrue(len(comment) >= 5508)

if __name__ == '__main__':
    unittest.main()
