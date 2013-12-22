#!/usr/bin/env python
"""
@author Karan Goel
@email karan@goel.im

The MIT License (MIT)
Copyright (c) 2013 Karan Goel

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import re
import time

from .utils import get_soup, get_item_soup
from .constants import BASE_URL, INTERVAL_BETWEEN_REQUESTS


class HN(object):
    """
    The class that parses the HN page, and builds up all stories
    """


    def _get_next_page(self, soup):
        """
        Get the relative url of the next page (The "More" link at
        the bottom of the page)
        """
        table = soup.findChildren('table')[2] # the table with all submissions
        
        # the last row of the table contains the relative url of the next page
        return table.findChildren(['tr'])[-1].find('a').get('href')


    def _get_soups(self, page, page_limit=1):
        """
        Returns a list of soups bs4 objects for all pages in the chain starting
        from 'page' following up to page_limit links.
        \tpage_limit=1 implies just the top level page
        """
        soups = list() # will hold all soups
        soups.append(get_soup(page)) # get the first page

        while len(soups) < page_limit:
            # get as many pages as requested
            cur_soup = soups[-1] # get the last seen page's soup
            next_page = self._get_next_page(cur_soup).lstrip('//')
            next_soup = get_soup(next_page) # get the next soup
            if len(next_soup.findChildren('table')) != 0:
                # making sure we are on the right page... get it?
                soups.append(next_soup)
            else:
                break
            time.sleep(INTERVAL_BETWEEN_REQUESTS) # be a good citizen
        return soups

    def _get_zipped_rows(self, soup):
        """
        Returns all 'tr' tag rows as a list of tuples. Each tuple is for
        a single story.
        """
        table = soup.findChildren('table')[2] # the table with all submissions
        rows = table.findChildren(['tr'])[:-2] # get all rows but last 2
        # remove the spacing rows
        spacing = range(2, len(rows), 3) # indices of spacing tr's
        rows = [row for (i, row) in enumerate(rows) if (i not in spacing)]
        # rank, title, domain
        info = [row for (i, row) in enumerate(rows) if (i % 2 == 0)]
        # points, submitter, comments
        detail = [row for (i, row) in enumerate(rows) if (i % 2 != 0)]
        
        return zip(info, detail) # build a list of tuple for all post


    def _build_story(self, all_rows):
        """
        Builds and returns a list of stories (dicts) from the passed source.
        """
        all_stories = [] # list to hold all stories

        for (info, detail) in all_rows:

            #-- Get the into about a story --#
            info_cells = info.findAll('td') # split in 3 cells

            rank = int(info_cells[0].string[:-1])
            title = '%s' % info_cells[2].find('a').string
            link = info_cells[2].find('a').get('href')

            is_self = False # by default all stories are linking posts

            if link.find('http') is -1 : # the link doesn't contains "http" meaning an internal link
                link = '%s/%s' % (BASE_URL, link)
                domain = BASE_URL
                is_self = True
            else:
                domain = info_cells[2].find('span').string[2:-2] # slice " (abc.com) "
            #-- Get the into about a story --#

            #-- Get the detail about a story --#
            detail_cell = detail.findAll('td')[1] # split in 2 cells, we need only second
            detail_concern = detail_cell.contents # list of details we need, 5 count
            
            num_comments = -1
            
            if re.match(r'^(\d+)\spoint.*', detail_concern[0].string) is not None:
                # can be a link or self post
                points = int(re.match(r'^(\d+)\spoint.*', detail_concern[0].string).groups()[0])
                submitter = '%s' % detail_concern[2].string
                submitter_profile = '%s/%s' % (BASE_URL, detail_concern[2].get('href'))
                published_time = ' '.join(detail_concern[3].strip().split()[:3])
                comment_tag = detail_concern[4]
                story_id = int(re.match(r'.*=(\d+)', comment_tag.get('href')).groups()[0])
                comments_link = '%s/item?id=%d' % (BASE_URL, story_id)
                comment_count = re.match(r'(\d+)\s.*', comment_tag.string)
                try:
                    # regex matched, cast to int
                    num_comments = int(comment_count.groups()[0])
                except AttributeError:
                    # did not match, assign 0
                    num_comments = 0
            else: # this is a job post
                points = 0
                submitter = ''
                submitter_profile = ''
                published_time = '%s' % detail_concern[0]
                comment_tag = ''
                try:
                    story_id = int(re.match(r'.*=(\d+)', link).groups()[0])
                except AttributeError:
                    story_id = -1 # job listing that points to external link
                comments_link = ''
                comment_count = -1
            #-- Get the detail about a story --#

            story = Story(rank, story_id, title, link, domain, points, submitter, 
                 published_time, submitter_profile, num_comments, comments_link,
                 is_self)
            
            all_stories.append(story)
        
        return all_stories


    def get_stories(self, story_type='', page_limit=1):
        """
        Returns a list of stories from the passed page
        of HN. 'story_type' can be:
        \t'' = top stories (homepage)
        \t'newest' = most recent stories
        \t'best' = best stories

        'page_limit' specifies the maximum number of pages to get.
        \tpage_limit=1 implies just the top level page
        """
        story = list()
        all_soups = self._get_soups(story_type, page_limit)
        for soup in all_soups:
            all_rows = self._get_zipped_rows(soup)
            story = story + self._build_story(all_rows)

        return story


class Story(object):
    """
    Story class represents one single story on HN
    """
    
    def __init__(self, rank, story_id, title, link, domain, points, submitter, 
                published_time, submitter_profile, num_comments, comments_link,
               is_self):
        self.rank = rank # the rank of story on the page
        self.story_id = story_id # the story's id
        self.title = title # the title of the story
        self.link = link # the url it points to (None for self posts)
        self.domain = domain # the domain of the link (None for self posts)
        self.points = points # the points/karma on the story
        self.submitter = submitter # the user who submitted the story
        self.published_time = published_time # publish time of story
        self.submitter_profile = submitter_profile # link to submitter's profile
        self.num_comments = num_comments # the number of comments it has
        self.comments_link = comments_link # the link to the comments page
        self.is_self = is_self # Truw is a self post

    def __repr__(self):
        """
        A string representation of the class object
        """
        return '<Story: ID={0}>'.format(self.story_id)
    
    def _build_comments(self, soup):
        """
        For the story, builds and returns a list of Comment objects.
        """
        table = soup.findChildren('table')[3] # the table holding all comments
        rows = table.findChildren(['tr']) # get all rows (each comment is duplicated twice)
        rows = [row for i, row in enumerate(rows) if (i % 2 == 0)] # now we have unique comments only
        
        comments = []
        
        if len(rows) > 1:
            for row in rows:
                
                ## Builds a flat list of comments
                
                # level of comment, starting with 0
                level = int(row.findChildren('td')[1].find('img').get('width')) // 40

                spans = row.findChildren('td')[3].findAll('span')
                # span[0] = submitter details
                # [<a href="user?id=jonknee">jonknee</a>, u' 1 hour ago  | ', <a href="item?id=6910978">link</a>]
                # span[1] = actual comment

                if str(spans[0]) != '<span class="comhead"></span>':
                    user = spans[0].contents[0].string # user who submitted the comment
                    time_ago = spans[0].contents[1].string.strip().rstrip(' |') # relative time of comment
                    comment_id = int(re.match(r'item\?id=(.*)', spans[0].contents[2].get('href')).groups()[0])
                
                    body = spans[1].text # text representation of comment (unformatted)
                    # html of comment, may not be valid
                    pat = re.compile(r'<span class="comment"><font color=".*">(.*)</font></span>')
                    body_html = re.match(pat, str(spans[1]).replace('\n', '')).groups()[0]
                else:
                    # comment deleted
                    user = ''
                    time_ago = ''
                    comment_id = -1
                    body = '[deleted]'
                    body_html = '[deleted]'

                comment = Comment(comment_id, level, user, time_ago, body, body_html)
                comments.append(comment)
            
        return comments
        
    def get_comments(self):
        """
        Returns a list of Comment(s) for the given story
        """
        soup = get_item_soup(self.story_id)
        return self._build_comments(soup)


class Comment(object):
    """
    Represents a comment on a post on HN
    """
    
    def __init__(self, comment_id, level, user, time_ago, body, body_html):
        self.comment_id = comment_id # the comment's item id
        self.level = level # commen's nesting level
        self.user = user # user's name who submitted the post
        self.time_ago = time_ago # time when it was submitted
        self.body = body # text representation of comment (unformatted)
        self.body_html = body_html # html of comment, may not be valid

    def __repr__(self):
        """
        A string representation of the class object
        """
        return '<Comment: ID={0}>'.format(self.comment_id)