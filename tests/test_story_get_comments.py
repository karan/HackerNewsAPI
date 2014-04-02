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

        self.story = Story.fromid(7324236)

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_get_comments_len(self):
        """
        Tests whether or not len(get_comments) > 90 if there are multiple pages
        of comments.
        """
        comments = self.story.get_comments()
        soup = utils.get_item_soup(7324236)
        more_button_present = False
        for anchor in soup.find_all('a'):
            if 'More' in anchor.text:
                more_button_present = True

        # Note: Hacker News is not consistent about the number of comments per
        # page. On multiple comment page stories, the number of comments on a
        # page is never less than 90. On single comment page stories, the
        # number of comments on the sole page is always less than 110.
        if more_button_present:
            self.assertTrue(len(comments) > 90)
        else:
            print comments, len(comments)
            self.assertTrue(len(comments) < 110)

    def test_comment_not_null(self):
        """
        Tests for null comments.
        """
        comments = self.story.get_comments()
        comment = comments[randrange(0, len(comments))]
        self.assertTrue(bool(comment.body))
        self.assertTrue(bool(comment.body_html))


if __name__ == '__main__':
    unittest.main()
