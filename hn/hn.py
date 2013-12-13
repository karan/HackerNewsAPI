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

from bs4 import BeautifulSoup
import requests


BASE_URL = 'https://news.ycombinator.com'
INTERVAL_BETWEEN_REQUESTS = 1 # seconds to sleep between 2 consecutive page requests

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
        soups.append(self._get_soup(page)) # get the first page

        while len(soups) < page_limit:
            # get as manu pages as requested
            cur_soup = soups[-1] # get the last seen page's soup
            next_page = self._get_next_page(cur_soup).lstrip('//')
            next_soup = self._get_soup(next_page) # get the next soup
            if len(next_soup.findChildren('table')) != 0:
                # making sure we are on the right page... get it?
                soups.append(next_soup)
            else:
                break
            time.sleep(INTERVAL_BETWEEN_REQUESTS) # be a good citizen
        return soups


    def _get_soup(self, page=''):
        """
        Returns a bs4 object of the page requested
        """
        content = requests.get('%s/%s' % (BASE_URL, page)).text
        return BeautifulSoup(content)


    def _get_zipped_rows(self, soup):
        """
        Returns all 'tr' tag rows as a list of tuples. Each tuple is for
        a single story.
        """
        table = soup.findChildren('table')[2] # the table with all submissions
        rows = table.findChildren(['tr'])[:-2] # get all rows but last 2
        # remove the spacing rows
        try:
            spacing = xrange(2, len(rows), 3) # indices of spacing tr's
        except:
            spacing = range(2, len(rows), 3) # indices of spacing tr's python3
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
            title = u'%s' % info_cells[2].find('a').string
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
                submitter = u'%s' % detail_concern[2].string
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
                published_time = u'%s' % detail_concern[0]
                comment_tag = ''
                try:
                    story_id = int(re.match(r'.*=(\d+)', link).groups()[0])
                except AttributeError:
                    story_id = -1 # job listing that points to external link
                comments_link = ''
                comment_count = -1
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