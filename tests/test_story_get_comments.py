import unittest

from hn import Story
from hn import utils
from random import randrange

class TestStoryGetComments(unittest.TestCase):

    def setUp(self):
        self.story = Story.fromid(7324236)

    def tearDown(self):
        pass

    def test_get_comments_len(self):
        """
        Tests whether or not len(get_comments) > 90 if there are multiple pages
        of comments.
        """
        comments = story.get_comments()
        soup = utils.get_item_soup(7324236)
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
            self.assertTrue(len(comments) < 110)

    def test_comment_not_null(self):
        """
        Tests for null comments.
        """
        comments = story.get_comments()
        comment = comments[randrange(0, len(comments))]
        self.assertTrue(bool(comment.body))
        self.assertTrue(bool(comment.body_html))
