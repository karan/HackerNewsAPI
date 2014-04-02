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
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'item?id=7324236'), 
            body=get_content('7324236.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'x?fnid=0MonpGsCkcGbA7rcbd2BAP'), 
            body=get_content('7324236-2.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'x?fnid=jyhCSQtM6ymFazFplS4Gpf'), 
            body=get_content('7324236-3.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'x?fnid=s3NA4qB6zMT3KHVk1x2MTG'), 
            body=get_content('7324236-4.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'x?fnid=pFxm5XBkeLtmphVejNZWlo'), 
            body=get_content('7324236-5.html'))

        story = Story.fromid(7324236)
        self.comments = story.get_comments()

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_get_comments_len(self):
        """
        Tests whether or not len(get_comments) > 90 if there are multiple pages
        of comments.
        """
        # Note: Hacker News is not consistent about the number of comments per
        # page. On multiple comment page stories, the number of comments on a
        # page is never less than 90. On single comment page stories, the
        # number of comments on the sole page is always less than 110.
        self.assertTrue(len(self.comments) > 90)

    def test_comment_not_null(self):
        """
        Tests for null comments.
        """
        comment = self.comments[randrange(0, len(self.comments))]
        self.assertTrue(bool(comment.body))
        self.assertTrue(bool(comment.body_html))

    def test_get_nested_comments(self):
        comment = self.comments[0].body
        self.assertEqual(comment.index("Healthcare.gov"), 0)

if __name__ == '__main__':
    unittest.main()
