#!/usr/bin/env python

from hn import HN

hn = HN()

'''
# print top 10 stories from homepage
for story in hn.get_stories():
    print story
    print '*' * 50
    print ''
'''
'''
# print 10 latest stories
for story in hn.get_stories(story_type='newest')[:10]:
    story["title"]
    print '*' * 50
    print ''
'''

'''
# print the top 10 stories from /best page
for story in hn.get_stories(story_type='best')[:10]:
    print story["title"]
    print '*' * 50
    print ''
'''

stories = hn.get_stories(story_type='best', page_limit=5)
print len(stories)

print stories