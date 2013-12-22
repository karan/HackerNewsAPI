#!/usr/bin/env python

from hn import HN

hn = HN()



# print top stories from homepage
for story in hn.get_stories():
    print(story.title)
    #print('[{0}] "{1}" by {2}'.format(story.points, story.title, story.submitter))

'''
# print 10 latest stories
for story in hn.get_stories(story_type='newest')[:10]:
    story.title
    print('*' * 50)
    print('')

# print the top 10 stories from /best page
for story in hn.get_stories(story_type='best')[:10]:
    print(story.title)
    print('*' * 50)
    print('')

'''

'''
# for each story on front page, print top comment
for story in hn.get_stories():
    print(story.title)
    comments = story.get_comments()
    print(comments[0] if len(comments) > 0 else None)
    print('*' * 10)
'''

'''
# for top 5 comments with nesting for top 5 stories
for story in hn.get_stories()[:5]:
    print(story.title)
    comments = story.get_comments()
    if len(comments) > 0:
        for comment in comments[:5]:
            print('\t' * (comment.level + 1) + comment.body[:min(30, len(comment.body))])
    print('*' * 10)
'''