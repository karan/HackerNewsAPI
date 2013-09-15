#!/usr/bin/env python
"""
@author Karan Goel
@email karan@goel.im

Copyright (C) 2013  Karan Goel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import re

from bs4 import BeautifulSoup
import requests


BASE_URL = 'http://news.ycombinator.com'


class HN(object):
    """
    The class that parses the HN page, and builds up all stories
    """
    
    
    def __get_soup(self, page=''):
        """
        Returns a bs4 object of the page requested
        """
        content = requests.get('%s/%s' % (BASE_URL, page)).text
        return BeautifulSoup(content)
    
    
    def __get_zipped_rows(self, soup):
        """
        Returns all 'tr' tag rows as a list of tuples. Each tuple is for
        a single story.
        """
        table = soup.findChildren('table')[2] # the table with all submissions
        rows = table.findChildren(['tr'])[:-2] # get all rows but last 2
        # remove the spacing rows
        spacing = xrange(2, len(rows), 3) # indices of spacing tr's
        rows = [row for (i, row) in enumerate(rows) if (i not in spacing)]
        # rank, title, domain
        info = [row for (i, row) in enumerate(rows) if (i % 2 == 0)]
        # points, submitter, comments
        detail = [row for (i, row) in enumerate(rows) if (i % 2 != 0)]

        return zip(info, detail) # build a list of tuple for all post
    
    
    def __build_story(self, all_rows):
        """
        Builds and returns a list of stories (dicts) from the passed source.
        """
        all_stories = [] # list to hold all stories
        
        for (info, detail) in all_rows:

            #-- Get the into about a story --#
            info_cells = info.findAll('td') # split in 3 cells
            
            rank = int(info_cells[0].string[:-1])
            title = info_cells[2].find('a').string
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

            if re.match(r'^(\d+)\spoint.*', detail_concern[0].string) is not None:
                # can be a link or self post
                points = int(re.match(r'^(\d+)\spoint.*', detail_concern[0].string).groups()[0])
                submitter = detail_concern[2].string
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
                submitter = None
                submitter_profile = None
                published_time = None
                comment_tag = None
                story_id = int(re.match(r'.*=(\d+)', link).groups()[0])
                comments_link = None
                comment_count = 0
            #-- Get the detail about a story --#
            
            story = {
                "rank": rank, 
                "story_id": story_id, 
                "title": title, 
                "link": link, 
                "domain": domain, 
                "points": points, 
                "submitter": submitter, 
                "published_time": published_time, 
                "submitter_profile": submitter_profile, 
                "num_comments": num_comments, 
                "comments_link": comments_link, 
                "is_self": is_self

            }
            all_stories.append(story)
            
        return all_stories
    
    
    def get_stories(self, story_type=''):
        """
        Returns a list of stories from the passed page
        of HN. 'story_type' can be:
        '' = top stories (homepage)
        'newest' = most recent stories
        'best' = best stories
        """
        all_rows = self.__get_zipped_rows(self.__get_soup(page=story_type))
        return self.__build_story(all_rows)