#!/usr/bin/env python

from hn import HN

hn = HN()


# print top 10 stories from homepage
for story in hn.get_stories()[:10]:
    print story["points"], story["title"], story["is_self"]
    print '*' * 50
    print ''

"""
# print 10 latest stories
for story in hn.get_stories(story_type='newest')[:10]:
    story["title"]
    print '*' * 50
    print ''
"""

# print all self posts from the homepage
for story in hn.get_stories():
    if story["is_self"]:
        story["title"]
        print '*' * 50
        print ''

"""
# print the top 10 stories from /best page
for story in hn.get_stories(story_type='best')[:10]:
    story["title"]
    print '*' * 50
    print ''
"""