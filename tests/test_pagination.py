from hn import HN

hn = HN()

def test_pagination_top():
    """
    This test checks if the pagination works for the front page by comparing
    number of stories in 2 pages.
    """
    assert len(hn.get_stories(page_limit=2)) == 2 * 30


def test_pagination_newest():
    """
    This test checks if the pagination works for the best page by comparing
    number of stories in 3 pages.
    """
    assert len(hn.get_stories(story_type='newest', page_limit=3)) == 3 * 30


def test_pagination_best():
    """
    This test checks if the pagination works for the top stories by comparing
    number of stories in 5 pages.
    """
    assert len(hn.get_stories(story_type='best', page_limit=5)) == 5 * 30
