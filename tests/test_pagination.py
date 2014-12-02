import unittest
from os import path
import sys

# from hn import HN, Story
# from hn import utils, constants

# from test_utils import get_content, PRESETS_DIR

# import httpretty

# class TestPagination(unittest.TestCase):

    # def setUp(self):
    #     httpretty.HTTPretty.enable()
    #     httpretty.register_uri(httpretty.GET,
    #                            'https://news.ycombinator.com/',
    #                            body=get_content('index.html'))
    #     httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
    #                                                      'best'),
    #                            body=get_content('best.html'))
    #     httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
    #                                                      'newest'),
    #                            body=get_content('newest.html'))
    #     httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
    #                                                      'x?fnid=WK2fLO5cPAJ9DnZbm8XOFR'),
    #                            body=get_content('best2.html'))
    #     httpretty.register_uri(httpretty.GET, '%s/%s' % (constants.BASE_URL,
    #                                                      'news2'),
    #                            body=get_content('news2.html'))

#         # check py version
#         self.PY2 = sys.version_info[0] == 2
#         self.hn = HN()

#     def tearDown(self):
#         httpretty.HTTPretty.disable()

#     # def test_more_link_top(self):
#     #     """
#     #     Checks if the "More" link at the bottom of homepage works.
#     #     """
#     #     soup = utils.get_soup()
#     #     fnid = self.hn._get_next_page(soup)[-5:]
#     #     expected = 'news2'
#     #     self.assertEqual(len(fnid), len(expected))

#     # def test_more_link_best(self):
#     #     """
#     #     Checks if the "More" link at the bottom of best page works.
#     #     """
#     #     soup = utils.get_soup(page='best')
#     #     fnid = self.hn._get_next_page(soup)[-29:]
#     #     expected = 'x?fnid=te9bsVN2BAx0XOpRmUjcY4'
#     #     self.assertEqual(len(fnid), len(expected))

#     # def test_more_link_newest(self):
#     #     """
#     #     Checks if the "More" link at the bottom of newest page works.
#     #     """
#     #     soup = utils.get_soup(page='newest')
#     #     fnid = self.hn._get_next_page(soup)[-29:]
#     #     expected = 'x?fnid=te9bsVN2BAx0XOpRmUjcY4'
#     #     self.assertEqual(len(fnid), len(expected))

#     def test_get_zipped_rows(self):
#         """
#         Tests HN._get_zipped_rows for best page.
#         """
#         soup = utils.get_soup(page='best')
#         rows = self.hn._get_zipped_rows(soup)
#         if self.PY2:
#             self.assertEqual(len(rows), 30)
#         else:
#             rows = [row for row in rows]
#             self.assertEqual(len(rows), 30)

#     def test_pagination_top_for_0_limit(self):
#         """
#         Checks if the pagination works for 0 limit.
#         """
#         stories = [story for story in self.hn.get_stories(limit=0)]
#         self.assertEqual(len(stories), 30)

#     def test_pagination_top_for_2_pages(self):
#         """
#         Checks if the pagination works for the front page.
#         """
#         stories = [story for story in self.hn.get_stories(limit=2*30)]
#         self.assertEqual(len(stories), 2 * 30)

#     def test_pagination_newest_for_3_pages(self):
#         """
#         Checks if the pagination works for the newest page.
#         """
#         stories = [story for story in self.hn.get_stories(story_type='newest', limit=3*30)]
#         self.assertEqual(len(stories), 3 * 30)

#     def test_pagination_best_for_2_pages(self):
#         """
#         Checks if the pagination works for the best page.
#         """
#         stories = [story for story in self.hn.get_stories(story_type='best', limit=2*30)]
#         self.assertEqual(len(stories), 2 * 30)


# if __name__ == '__main__':
#     unittest.main()
