#!/usr/bin/env python

from hn import HN, Story

hn = HN()

top_iter = hn.get_stories(limit=60) # a generator over 60 stories from top page


# print top stories from homepage
for story in top_iter:
    print(story.title)
    #print('[{0}] "{1}" by {2}'.format(story.points, story.title, story.submitter))


# print 10 latest stories
for story in hn.get_stories(story_type='newest', limit=10):
    story.title
    print('*' * 50)
    print('')


# for each story on front page, print top comment
for story in hn.get_stories():
    print(story.title)
    comments = story.get_comments()
    print(comments[0] if len(comments) > 0 else None)
    print('*' * 10)



# print top 5 comments with nesting for top 5 stories
for story in hn.get_stories(story_type='best', limit=5):
    print(story.title)
    comments = story.get_comments()
    if len(comments) > 0:
        for comment in comments[:5]:
            print('\t' * (comment.level + 1) + comment.body[:min(30, len(comment.body))])
    print('*' * 10)

# get the comments from any custom story
story = Story.fromid(6374031)
comments = story.get_comments()