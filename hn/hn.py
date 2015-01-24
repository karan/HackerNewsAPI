#!/usr/bin/env python

"""
Hacker News API
Unofficial Python API for Hacker News.

@author Karan Goel
@email karan@goel.im
"""

import re

from .utils import get_soup, get_item_soup
from .constants import BASE_URL


class HN(object):
    """
    The class that parses the HN page, and builds up all stories
    """

    def __init__(self):
        self.more = ''

    # def _get_next_page(self, soup):
    #     """
    #     Get the relative url of the next page (The "More" link at
    #     the bottom of the page)
    #     """
    #     table = soup.findChildren('table')[2]  # table with all submissions
    #     # the last row of the table contains the relative url of the next
    #     # page
    #     return table.findChildren(['tr'])[-1].find('a').get('href').replace(
    #         BASE_URL, '').lstrip('//')

    def _get_zipped_rows(self, soup):
        """
        Returns all 'tr' tag rows as a list of tuples. Each tuple is for
        a single story.
        """
        # the table with all submissions
        table = soup.findChildren('table')[2]
        # get all rows but last 2
        rows = table.findChildren(['tr'])[:-2]
        # remove the spacing rows
        # indices of spacing tr's
        spacing = range(2, len(rows), 3)
        rows = [row for (i, row) in enumerate(rows) if (i not in spacing)]
        # rank, title, domain
        info = [row for (i, row) in enumerate(rows) if (i % 2 == 0)]
        # points, submitter, comments
        detail = [row for (i, row) in enumerate(rows) if (i % 2 != 0)]

        # build a list of tuple for all post
        return zip(info, detail)

    def _build_story(self, all_rows):
        """
        Builds and returns a list of stories (dicts) from the passed source.
        """
        # list to hold all stories
        all_stories = []

        for (info, detail) in all_rows:

            #-- Get the into about a story --#
            # split in 3 cells
            info_cells = info.findAll('td')

            rank = int(info_cells[0].string[:-1])
            title = '%s' % info_cells[2].find('a').string
            link = info_cells[2].find('a').get('href')

            # by default all stories are linking posts
            is_self = False

            # the link doesn't contains "http" meaning an internal link
            if link.find('item?id=') is -1:
                # slice " (abc.com) "
                domain = info_cells[2].findAll('span')[1].string[2:-1]
            else:
                link = '%s/%s' % (BASE_URL, link)
                domain = BASE_URL
                is_self = True
            #-- Get the into about a story --#

            #-- Get the detail about a story --#
            # split in 2 cells, we need only second
            detail_cell = detail.findAll('td')[1]
            # list of details we need, 5 count
            detail_concern = detail_cell.contents

            num_comments = -1

            if re.match(r'^(\d+)\spoint.*', detail_concern[0].string) is not \
                    None:
                # can be a link or self post
                points = int(re.match(r'^(\d+)\spoint.*', detail_concern[
                    0].string).groups()[0])
                submitter = '%s' % detail_concern[2].string
                submitter_profile = '%s/%s' % (BASE_URL, detail_concern[
                    2].get('href'))
                published_time = ' '.join(detail_concern[3].strip().split()[
                                          :3])
                comment_tag = detail_concern[4]
                story_id = int(re.match(r'.*=(\d+)', comment_tag.get(
                    'href')).groups()[0])
                comments_link = '%s/item?id=%d' % (BASE_URL, story_id)
                comment_count = re.match(r'(\d+)\s.*', comment_tag.string)
                try:
                    # regex matched, cast to int
                    num_comments = int(comment_count.groups()[0])
                except AttributeError:
                    # did not match, assign 0
                    num_comments = 0
            else:
                # this is a job post
                points = 0
                submitter = ''
                submitter_profile = ''
                published_time = '%s' % detail_concern[0]
                comment_tag = ''
                try:
                    story_id = int(re.match(r'.*=(\d+)', link).groups()[0])
                except AttributeError:
                    # job listing that points to external link
                    story_id = -1
                comments_link = ''
                comment_count = -1
            #-- Get the detail about a story --#

            story = Story(rank, story_id, title, link, domain, points,
                          submitter, published_time, submitter_profile,
                          num_comments, comments_link, is_self)

            all_stories.append(story)

        return all_stories

    def get_stories(self, story_type='', limit=30):
        """
        Yields a list of stories from the passed page
        of HN.
        'story_type' can be:
        \t'' = top stories (homepage) (default)
        \t'news2' = page 2 of top stories
        \t'newest' = most recent stories
        \t'best' = best stories

        'limit' is the number of stories required from the given page.
        Defaults to 30. Cannot be more than 30.
        """
        if limit is None or limit < 1 or limit > 30:
            # we need at least 30 items
            limit = 30

        stories_found = 0
        # self.more = story_type
        # while we still have more stories to find
        while stories_found < limit:
            # get current page soup
            soup = get_soup(page=story_type)
            all_rows = self._get_zipped_rows(soup)
            # get a list of stories on current page
            stories = self._build_story(all_rows)
            # move to next page
            # self.more = self._get_next_page(soup)

            for story in stories:
                yield story
                stories_found += 1

                # if enough stories found, return
                if stories_found == limit:
                    return

    def get_leaders(self, limit=10):
        """ Return the leaders of Hacker News """
        if limit is None:
            limit = 10
        soup = get_soup('leaders')
        table = soup.find('table')
        leaders_table = table.find_all('table')[1]
        listleaders = leaders_table.find_all('tr')[2:]
        listleaders.pop(10)  # Removing because empty in the Leaders page
        for i, leader in enumerate(listleaders):
            if i == limit:
                return
            if not leader.text == '':
                item = leader.find_all('td')
                yield User(item[1].text, '', item[2].text, item[3].text)


class Story(object):
    """
    Story class represents one single story on HN
    """

    def __init__(self, rank, story_id, title, link, domain, points,
                 submitter, published_time, submitter_profile, num_comments,
                 comments_link, is_self):
        self.rank = rank  # the rank of story on the page
        self.story_id = story_id  # the story's id
        self.title = title  # the title of the story
        self.link = link  # the url it points to (None for self posts)
        self.domain = domain  # the domain of the link (None for self posts)
        self.points = points  # the points/karma on the story
        self.submitter = submitter  # the user who submitted the story
        self.published_time = published_time  # publish time of story
        self.submitter_profile = submitter_profile  # link to submitter profile
        self.num_comments = num_comments  # the number of comments it has
        self.comments_link = comments_link  # the link to the comments page
        self.is_self = is_self  # Truw is a self post

    def __repr__(self):
        """
        A string representation of the class object
        """
        return '<Story: ID={0}>'.format(self.story_id)

    def _get_next_page(self, soup, current_page):
        """
        Get the relative url of the next page (The "More" link at
        the bottom of the page)
        """

        # Get the table with all the comments:
        if current_page == 1:
            table = soup.findChildren('table')[3]
        elif current_page > 1:
            table = soup.findChildren('table')[2]

        # the last row of the table contains the relative url of the next page
        anchor = table.findChildren(['tr'])[-1].find('a')
        if anchor and anchor.text == u'More':
            return anchor.get('href').lstrip(BASE_URL)
        else:
            return None

    def _build_comments(self, soup):
        """
        For the story, builds and returns a list of Comment objects.
        """

        comments = []
        current_page = 1

        while True:
            # Get the table holding all comments:
            if current_page == 1:
                table = soup.findChildren('table')[3]
            elif current_page > 1:
                table = soup.findChildren('table')[2]
            # get all rows (each comment is duplicated twice)
            rows = table.findChildren(['tr'])
            # last row is more, second last is spacing
            rows = rows[:len(rows) - 2]
            # now we have unique comments only
            rows = [row for i, row in enumerate(rows) if (i % 2 == 0)]

            if len(rows) > 1:
                for row in rows:

                    # skip an empty td
                    if not row.findChildren('td'):
                        continue

                    # Builds a flat list of comments

                    # level of comment, starting with 0
                    level = int(row.findChildren('td')[1].find('img').get(
                        'width')) // 40

                    spans = row.findChildren('td')[3].findAll('span')
                    # span[0] = submitter details
                    # [<a href="user?id=jonknee">jonknee</a>, u' 1 hour ago  | ', <a href="item?id=6910978">link</a>]
                    # span[1] = actual comment

                    if str(spans[0]) != '<span class="comhead"></span>':
                        # user who submitted the comment
                        user = spans[0].contents[0].string
                        # relative time of comment
                        time_ago = spans[0].contents[1].string.strip(
                        ).rstrip(' |')
                        try:
                            comment_id = int(re.match(r'item\?id=(.*)',
                                                      spans[0].contents[
                                                          2].get(
                                                          'href')).groups()[0])
                        except AttributeError:
                            comment_id = int(re.match(r'%s/item\?id=(.*)' %
                                                      BASE_URL,
                                                      spans[0].contents[
                                                          2].get(
                                                          'href')).groups()[0])

                        # text representation of comment (unformatted)
                        body = spans[1].text

                        if body[-2:] == '--':
                            body = body[:-5]

                        # html of comment, may not be valid
                        try:
                            pat = re.compile(
                                r'<span class="comment"><font color=".*">(.*)</font></span>')
                            body_html = re.match(pat, str(spans[1]).replace(
                                '\n', '')).groups()[0]
                        except AttributeError:
                            pat = re.compile(
                                r'<span class="comment"><font color=".*">(.*)</font></p><p><font size="1">')
                            body_html = re.match(pat, str(spans[1]).replace(
                                '\n', '')).groups()[0]

                    else:
                        # comment deleted
                        user = ''
                        time_ago = ''
                        comment_id = -1
                        body = '[deleted]'
                        body_html = '[deleted]'

                    comment = Comment(comment_id, level, user, time_ago,
                                      body, body_html)
                    comments.append(comment)

            # Move on to the next page of comments, or exit the loop if there
            # is no next page.
            next_page_url = self._get_next_page(soup, current_page)
            if not next_page_url:
                break

            soup = get_soup(page=next_page_url)
            current_page += 1

        previous_comment = None
        # for comment in comments:
        # if comment.level == 0:
        #         previous_comment = comment
        #     else:
        #         level_difference = comment.level - previous_comment.level
        #         previous_comment.body_html += '\n' + '\t' * level_difference \
        #                                       + comment.body_html
        #         previous_comment.body += '\n' + '\t' * level_difference + \
        #                                  comment.body
        return comments

    @classmethod
    def fromid(self, item_id):
        """
        Initializes an instance of Story for given item_id.
        It is assumed that the story referenced by item_id is valid
        and does not raise any HTTP errors.
        item_id is an int.
        """
        if not item_id:
            raise Exception('Need an item_id for a story')
        # get details about a particular story
        soup = get_item_soup(item_id)

        # this post has not been scraped, so we explititly get all info
        story_id = item_id
        rank = -1

        # to extract meta information about the post
        info_table = soup.findChildren('table')[2]
        # [0] = title, domain, [1] = points, user, time, comments
        info_rows = info_table.findChildren('tr')

        # title, domain
        title_row = info_rows[0].findChildren('td')[1]
        title = title_row.find('a').text
        try:
            domain = title_row.find('span').string[2:-2]
            # domain found
            is_self = False
            link = title_row.find('a').get('href')
        except AttributeError:
            # self post
            domain = BASE_URL
            is_self = True
            link = '%s/item?id=%s' % (BASE_URL, item_id)

        # points, user, time, comments
        meta_row = info_rows[1].findChildren('td')[1].contents
        # [<span id="score_7024626">789 points</span>, u' by ', <a href="user?id=endianswap">endianswap</a>,
        # u' 8 hours ago  | ', <a href="item?id=7024626">238 comments</a>]

        points = int(re.match(r'^(\d+)\spoint.*', meta_row[0].text).groups()[0])
        submitter = meta_row[2].text
        submitter_profile = '%s/%s' % (BASE_URL, meta_row[2].get('href'))
        published_time = ' '.join(meta_row[3].strip().split()[:3])
        comments_link = '%s/item?id=%s' % (BASE_URL, item_id)
        try:
            num_comments = int(re.match(r'(\d+)\s.*', meta_row[
                4].text).groups()[0])
        except AttributeError:
            num_comments = 0
        story = Story(rank, story_id, title, link, domain, points, submitter,
                      published_time, submitter_profile, num_comments,
                      comments_link, is_self)
        return story

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
        self.comment_id = comment_id  # the comment's item id
        self.level = level  # comment's nesting level
        self.user = user  # user's name who submitted the post
        self.time_ago = time_ago  # time when it was submitted
        self.body = body  # text representation of comment (unformatted)
        self.body_html = body_html  # html of comment, may not be valid

    def __repr__(self):
        """
        A string representation of the class object
        """
        return '<Comment: ID={0}>'.format(self.comment_id)


class User(object):
    """
    Represents a User on HN
    """

    def __init__(self, username, date_created, karma, avg):
        self.username = username
        self.date_created = date_created
        self.karma = karma
        self.avg = avg

    def __repr__(self):
        return '{0} {1} {2}'.format(self.username, self.karma, self.avg)
