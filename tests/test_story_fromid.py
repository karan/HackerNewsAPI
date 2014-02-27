import unittest
import sys

from hn import HN, Story
from hn import utils

class TestStoryFromId(unittest.TestCase):

    def setUp(self):
        # check py version
        self.PY2 = sys.version_info[0] == 2
        self.hn = HN()
        self.story = Story.fromid(6374031)

    def tearDown(self):
        pass

    def test_from_id_constructor(self):
        """
        Tests whether or not the constructor fromid works or not
        by testing the returned Story.
        """
        self.assertEqual(self.story.submitter, 'karangoeluw')
        self.assertEqual(self.story.title, 'Python API for Hacker News')
        self.assertFalse(self.story.is_self)

    def test_comment_for_fromid(self):
        """
        Tests if the comment scraping works for fromid or not.
        """
        comments = self.story.get_comments()
        self.assertEqual(len(comments), 31)
        self.assertEqual(comments[0].comment_id, 6374318)
        self.assertEqual(comments[2].level, 1)