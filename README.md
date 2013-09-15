![Hacker News API](https://raw.github.com/thekarangoel/HackerNewsAPI/master/HN.jpg)

Unofficial Python API for [Hacker News](https://news.ycombinator.com/).

[![Version](https://pypip.in/v/HackerNews/badge.png)](https://crate.io/packages/HackerNews/)   [![Downloads](https://pypip.in/d/HackerNews/badge.png)](https://crate.io/packages/HackerNews/)

Installation
============

    $ pip install HackerNews


[Donate](https://www.gittip.com/Karan%20Goel/)
=============

If you love and use *HackerNewsAPI*, please consider [donating via gittip](https://www.gittip.com/Karan%20Goel/). Any support is appreciated!

Classes
==========

## `HN`

The class that parses the HN page, and builds up all stories.

#### Methods

`get_stories(story_type='')` - Returns a list of stories from the passed page of HN. 'story_type' can be: '' = top stories (homepage), 'newest' = most recent stories, 'best' = best stories

#### Story details (keys of `dict`)

* **rank** - the rank of story on the page
* **story_id** - the story's id
* **title** - the title of the story
* **is_self** - true for self/job stories
* **link** - the url it points to (None for self posts)
* **domain** - the domain of the link (None for self posts)
* **points** - the points/karma on the story
* **submitter** - the user who submitted the story
* **submitter_link** - the above user profile link
* **published_time** - the published time ago
* **num_comments** - the number of comments it has
* **comments_link** - the link to the comments page

Example
========

See [`test_bot.py`](https://github.com/thekarangoel/HackerNewsAPI/blob/master/test_bot.py)
        
Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
