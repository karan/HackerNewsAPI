#!/usr/bin/env python

from urllib2 import urlopen

from bs4 import BeautifulSoup


class HN():
    """The class that parses the HN page, and builds up all Story objects"""
    
    def get_zipped_rows(self, soup):
        """Returns all 'tr' tag rows as a list of tuples. Each tuple is for
        a single story."""
        table = soup.findChildren('table')[2] # the table with all submissions
        rows = table.findChildren(['tr'])[:-2] # get all rows but last 2
        # remote the spacing rows
        spacing = xrange(2, len(rows), 3) # indices of spacing tr's
        rows = [row for (i, row) in enumerate(rows) if (i not in spacing)]
        # rank, title, domain
        info = [row for (i, row) in enumerate(rows) if (i % 2 == 0)]
        # points, submitter, comments
        detail = [row for (i, row) in enumerate(rows) if (i % 2 != 0)]

        return zip(info, detail) # build a list of tuple for all post
    
    def get_top_stories(self):
        """Returns a list of Story objects from the homepage
        of HN"""
        content = urlopen('http://news.ycombinator.com/').read()
        soup = BeautifulSoup(content)
        all_rows = self.get_zipped_rows(soup)
        return all_rows
        
    def get_newest_stories(self):
        """Returns a list of Story objects from the newest page
        of HN"""
        content = urlopen('http://news.ycombinator.com/newest').read()
        soup = BeautifulSoup(content)
        all_rows = self.get_zipped_rows(soup)
    

class Story():
    """Story class represents one single story on HN"""
    
    def __init__(self, rank, story_id, title, link, domain, points, submitter, 
                 num_comments, comments_link):
        self.rank = rank
        self.story_id = story_id
        self.title = title
        self.link = link
        self.domain = domain
        self.points = points
        self.submitter = submitter
        self.num_comments = num_comments
        self.comments_link = comments_link

    def print_story(self):
        """Print the details of a story"""
        print 'Rank: %d' % self.rank
        print 'Story ID: %d' % self.story_id
        print 'Title: %d' % self.title
        print 'Link: %d' % self.link
        print 'Domain: %d' % self.domain
        print 'Points: %d' % self.points
        print 'Submitted by: %d' % self.submitter
        print 'Number of comments: %d' % self.num_comments
        print 'Link to comments: %d' % self.comments_link
    
    def __repr__(self):
        """A string representation of the class object"""
        return '{0} by {1}'.format(self.title, self.submitter)