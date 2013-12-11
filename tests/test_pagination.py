from hn import HN

hn = HN()

def test_pagination_top_for_2_pages():
    """
    This test checks if the pagination works for the front page by comparing
    number of stories in 2 page.
    """
    stories = hn.get_stories(page_limit=2)
    assert len(stories) == 2 * 30


def test_pagination_newest_for_3_pages():
    """
    This test checks if the pagination works for the best page by comparing
    number of stories in 3 pages.
    """
    stories = hn.get_stories(story_type='newest', page_limit=3)
    assert len(stories) == 3 * 30


def test_pagination_best_for_5_pages():
    """
    This test checks if the pagination works for the best stories by comparing
    number of stories in 5 pages.
    """
    stories = hn.get_stories(story_type='best', page_limit=5)
    assert len(stories) == 5 * 30

def test_pagination_top_for_0_pages():
    """
    This test checks if the pagination works for the top stories by comparing
    number of stories in 0 page.
    """
    stories = hn.get_stories(page_limit=0)
    assert len(stories) == 1 * 30

def test_pagination_top_for_negative_pages():
    """
    This test checks if the pagination works for the top stories by comparing
    number of stories in negative page.
    """
    stories = hn.get_stories(page_limit=-10)
    assert len(stories) == 1 * 30
