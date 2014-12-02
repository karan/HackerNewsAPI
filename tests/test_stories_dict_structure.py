import unittest
from os import path
import sys

from hn import HN, Story
from hn import utils, constants

from test_utils import get_content, PRESETS_DIR

import httpretty


class TestStoriesDict(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(httpretty.GET,
                               'https://news.ycombinator.com/',
                               body=get_content('index.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
                                                         'best'),
                               body=get_content('best.html'))
        httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
                                                         'newest'),
                               body=get_content('newest.html'))

        # check py version
        PY2 = sys.version_info[0] == 2
        if not PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]

        self.hn = HN()
        self.top_stories = [story for story in self.hn.get_stories()]
        self.newest_stories = [story for story in self.hn.get_stories(
            story_type='newest')]
        self.best_stories = [story for story in self.hn.get_stories(
            story_type='best')]

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_stories_dict_structure_top(self):
        """
        Checks data type of each field of each story from front page.
        """
        for story in self.top_stories:
            # testing for unicode or string
            # because the types are mixed sometimes
            assert type(story.rank) == int
            assert type(story.story_id) == int
            assert type(story.title) in self.text_type
            assert type(story.link) in self.text_type
            assert type(story.domain) in self.text_type
            assert type(story.points) == int
            assert type(story.submitter) in self.text_type
            assert type(story.published_time) in self.text_type
            assert type(story.submitter_profile) in self.text_type
            assert type(story.num_comments) == int
            assert type(story.comments_link) in self.text_type
            assert type(story.is_self) == bool

    def test_stories_dict_structure_newest(self):
        """
        Checks data type of each field of each story from newest page
        """
        for story in self.newest_stories:
            # testing for unicode or string
            # because the types are mixed sometimes
            assert type(story.rank) == int
            assert type(story.story_id) == int
            assert type(story.title) in self.text_type
            assert type(story.link) in self.text_type
            assert type(story.domain) in self.text_type
            assert type(story.points) == int
            assert type(story.submitter) in self.text_type
            assert type(story.published_time) in self.text_type
            assert type(story.submitter_profile) in self.text_type
            assert type(story.num_comments) == int
            assert type(story.comments_link) in self.text_type
            assert type(story.is_self) == bool

    def test_stories_dict_structure_best(self):
        """
        Checks data type of each field of each story from best page
        """
        for story in self.best_stories:
            # testing for unicode or string
            # because the types are mixed sometimes
            assert type(story.rank) == int
            assert type(story.story_id) == int
            assert type(story.title) in self.text_type
            assert type(story.link) in self.text_type
            assert type(story.domain) in self.text_type
            assert type(story.points) == int
            assert type(story.submitter) in self.text_type
            assert type(story.published_time) in self.text_type
            assert type(story.submitter_profile) in self.text_type
            assert type(story.num_comments) == int
            assert type(story.comments_link) in self.text_type
            assert type(story.is_self) == bool

    def test_stories_dict_length_top(self):
        """
        Checks if the dict returned by scraping the front page of HN is 30.
        """
        self.assertEqual(len(self.top_stories), 30)

    def test_stories_dict_length_best(self):
        """
        Checks if the dict returned by scraping the best page of HN is 30.
        """
        self.assertEqual(len(self.best_stories), 30)

    def test_stories_dict_length_top_newest(self):
        """
        Checks if the dict returned by scraping the newest page of HN is 30.
        """
        self.assertEqual(len(self.newest_stories), 30)


if __name__ == '__main__':
    unittest.main()
