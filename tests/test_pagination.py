from hn import HN

hn = HN()

def test_pagination():
    """
    This test checks if the pagination works for the front page.
    """
    assert len(hn.get_stories(story_type='', follow_pagination_limit=1)) == 30+1*30


def test_pagination_newest():
    """
    This test checks if the pagination works for the best page.
    """
    assert len(hn.get_stories(story_type='newest', follow_pagination_limit=3)) == 30+3*30


def test_pagination_best():
    """
    This test checks if the pagination works for the top stories.
    """
    assert len(hn.get_stories(story_type='best', follow_pagination_limit=5)) == 30+5*30
