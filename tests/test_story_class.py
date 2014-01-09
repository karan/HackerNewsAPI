#!/usr/bin/env python

import unittest
import sys

from hn import HN, Story

class TestStory(unittest.TestCase):
    
    def setUp(self):
        self.PY2 = sys.version_info[0] == 2
        if not PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]
        self.story = Story('6115341') # https://news.ycombinator.com/item?id=6115341
    
    def tearDown(self):
        pass
    
    def test_story_repr(self):
        """
        Check string repr of the story.
        """
        self.assertEqual(self.story, '<Story: ID=6115341>')
    
    def test_story_data_types(self):
        """
        Test types of fields of a Story object
        """
        assert type(self.story.rank) == int
        assert type(self.story.self.story_id) == int
        assert type(self.story.title) in self.text_type
        assert type(self.story.link) in self.text_type
        assert type(self.story.domain) in self.text_type
        assert type(self.story.points) == int
        assert type(self.story.submitter) in self.text_type
        assert type(self.story.published_time) in self.text_type
        assert type(self.story.submitter_profile) in self.text_type
        assert type(self.story.num_comments) == int
        assert type(self.story.comments_link) in self.text_type
        assert type(self.story.is_self) == bool