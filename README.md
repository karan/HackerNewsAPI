HackerNewsAPI
=============

Unofficial Python wrapper for [Hacker News](https://news.ycombinator.com/).

Dependencies
============

**Beautiful Soup**

    $ pip install beautifulsoup

Classes
==========

## `HN`

The class that parses the HN page, and builds up all Story objects

#### Methods

`get_top_stories()` - Returns a list of Story objects from the homepage of HN

`get_newest_stories()` - Returns a list of Story objects from the newest page of HN

## `Story`

Story class represents one single story on HN

#### Methods

`print_story()` - Print the details of a story

#### Story details

* **rank** - the rank of story on the page
* **story_id** - the story's id
* **title** - the title of the story
* **link** - the url it points to (None for self posts)
* **domain** - the domain of the link (None for self posts)
* **points** - the points/karma on the story
* **submitter** - the user who submitted the story
* **num_comments** - the number of comments it has
* **comments_link** - the link to the comments page

Example
========

[`test_bot.py`](https://github.com/thekarangoel/HackerNewsAPI/blob/master/test_bot.py) prints top and new posts.

    #!/usr/bin/env python
    
    from hn import HN
    
    hn = HN()
    
    for story in hn.get_top_stories()[:10]:
        story.print_story()
        print '*' * 50
        print ''
    
    for story in hn.get_newest_stories()[:5]:
        story.print_story()
        print '*' * 50
        print ''
        
Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
