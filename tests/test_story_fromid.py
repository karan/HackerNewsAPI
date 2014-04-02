import unittest
from os import path
import sys

from hn import HN, Story
from hn import utils, constants

from test_utils import get_content, PRESETS_DIR

import httpretty

class TestStoryFromId(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(httpretty.GET, 'https://news.ycombinator.com/', 
            body=get_content('index.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL, 'item?id=6115341'), 
            body=get_content('6115341.html'))

        # check py version
        self.PY2 = sys.version_info[0] == 2
        self.hn = HN()
        self.story = Story.fromid(6115341)

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_from_id_constructor(self):
        """
        Tests whether or not the constructor fromid works or not
        by testing the returned Story.
        """
        self.assertEqual(self.story.submitter, 'karangoeluw')
        self.assertEqual(self.story.title, 'Github: What does the "Gold Star" next to my repository (in Explore page) mean?')
        self.assertTrue(self.story.is_self)

    def test_comment_for_fromid(self):
        """
        Tests if the comment scraping works for fromid or not.
        """
        comments = self.story.get_comments()
        self.assertEqual(len(comments), 3)
        self.assertEqual(comments[0].comment_id, 6115436)
        self.assertEqual(comments[2].level, 2)


if __name__ == '__main__':
    unittest.main()
