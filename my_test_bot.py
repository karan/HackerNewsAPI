#!/usr/bin/env python

from hn import HN

hn = HN()


# print top stories from homepage
for story in hn.get_stories():
    print(story)

'''
# print 10 latest stories
for story in hn.get_stories(story_type='newest')[:10]:
    story["title"]
    print('*' * 50)
    print('')

# print the top 10 stories from /best page
for story in hn.get_stories(story_type='best')[:10]:
    print(story["title"])
    print('*' * 50)
    print('')

stories = hn.get_stories(story_type='best', page_limit=5)
print(len(stories))

print(stories)
'''

'''
# for each story on front page, print top comment
for story in hn.get_stories():
    print(story)
    comments = story.get_comments()
    print(comments[0] if len(comments) > 0 else 0)
    print('*' * 10)
'''

'''
# for top 5 comments with nesting for top 5 stories
for story in hn.get_stories()[:5]:
    try:
        print(story)
        comments = story.get_comments()
        if len(comments) > 0:
            for comment in comments[:5]:
                print('\t' * (comment.level + 1)),
                print(str(comment))
    except UnicodeEncodeError:
        print(story.title)
    print('*' * 10)
'''