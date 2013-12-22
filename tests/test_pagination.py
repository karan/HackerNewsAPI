import unittest

from hn import HN

class TestPagination(unittest.TestCase):

    def setUp(self):
        self.hn = HN()
    
    def tearDown(self):
        pass
    
    def test_pagination_top_for_2_pages(self):
        """
        Checks if the pagination works for the front page.
        """
        stories = self.hn.get_stories(page_limit=2)
        self.assertEqual(len(stories), 2 * 30)
    
    def test_pagination_newest_for_3_pages(self):
        """
        Checks if the pagination works for the newest page.
        """
        stories = self.hn.get_stories(story_type='newest', page_limit=3)
        self.assertEqual(len(stories), 3 * 30)
        
    def test_pagination_best_for_2_pages(self):
        """
        Checks if the pagination works for the best page.
        """
        stories = self.hn.get_stories(story_type='best', page_limit=2)
        self.assertEqual(len(stories), 2 * 30)

if __name__ == '__main__':
    unittest.main()