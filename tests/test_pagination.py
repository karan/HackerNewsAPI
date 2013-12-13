from hn import HN

hn = HN()


def test_pagination_top_for_2_pages():
    """
    Checks if the pagination works for the front page.
    """
    stories = hn.get_stories(page_limit=2)
    assert len(stories) == 2 * 30

def test_pagination_newest_for_3_pages():
    """
    Checks if the pagination works for the newest page.
    """
    stories = hn.get_stories(story_type='newest', page_limit=3)
    assert len(stories) == 3 * 30

def test_pagination_best_for_2_pages():
    """
    Checks if the pagination works for the best page.
    """
    stories = hn.get_stories(story_type='best', page_limit=2)
    assert len(stories) == 2 * 30