#!/usr/bin/env python

from hn import HN

hn = HN()


# print top 10 stories from homepage
for story in hn.get_top_stories()[:10]:
    story.print_story()
    print '*' * 50
    print ''

# print 10 latest stories
for story in hn.get_newest_stories()[:10]:
    story.print_story()
    print '*' * 50
    print ''

# print all self posts from the homepage
for story in hn.get_top_stories():
    if story.is_self_post:
        story.print_story()
        print '*' * 50
        print ''