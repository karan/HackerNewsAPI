import unittest
from os import path
import sys
from random import randrange

from hn import HN, Story
from hn import utils, constants

from test_utils import get_content, PRESETS_DIR

import httpretty

class TestStoryGetComments(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(httpretty.GET, 'https://news.ycombinator.com/', 
            body=get_content('index.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'item?id=7404389'), 
            body=get_content('7404389.html'))
        self.story = Story.fromid(7404389)
        self.comments = self.story.get_comments()

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_get_nested_comments(self):
    	comment = self.comments[0].body
    	self.assertTrue(len(comment) == 5712)

if __name__ == '__main__':
    unittest.main()
