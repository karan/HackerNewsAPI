![Hacker News API](https://raw.github.com/karan/HackerNewsAPI/master/HN.jpg)

Unofficial Python API for [Hacker News](https://news.ycombinator.com/).


| Build Status | Test Coverage | Version | Download |
| ------------ | ------------- | ------- | -------- |
| [![Build Status](https://travis-ci.org/karan/HackerNewsAPI.png?branch=master)](https://travis-ci.org/karan/HackerNewsAPI) | [![Coverage Status](https://coveralls.io/repos/karan/HackerNewsAPI/badge.png)](https://coveralls.io/r/karan/HackerNewsAPI) | [![Version](https://pypip.in/v/HackerNews/badge.png)](https://crate.io/packages/HackerNews/) | [![Downloads](https://pypip.in/d/HackerNews/badge.png)](https://crate.io/packages/HackerNews/) |

Features
============

- Compatible with Python 2 and Python 3
- Supports 'top', 'newest' and 'best' posts
- Pagination
- Handles external posts, self posts and job posts

Installation
============

    $ pip install HackerNews


[Donate](https://www.gittip.com/Karan%20Goel/)
=============

If you love and use *HackerNewsAPI*, please consider [donating via gittip](https://www.gittip.com/Karan%20Goel/). Any support is appreciated!

Usage
==========

**NOTE:** Do not make a lot of requests in a short period of time. HN has it's own throttling system.


    from hn import HN

    hn = HN()
    
    # print the first 2 pages of newest stories
    for story in hn.get_stories(story_type='newest', page_limit=2):
        print story["rank"], story["title"]
        print

Each `story` has the following properties

- **rank** - the rank of story on the page (keep pagination in mind)
- **story_id** - the story's id
- **title** - the title of the story
- **is_self** - true for self/job stories
- **link** - the url it points to (`''` for self posts)
- **domain** - the domain of the link (`''` for self posts)
- **points** - the points/karma on the story
- **submitter** - the user who submitted the story (`''` for job posts)
- **submitter_profile** - the above user's profile link (can be `''`)
- **published_time** - the published time
- **num_comments** - the number of comments a story has
- **comments_link** - the link to the comments page

Example
========

See [`my_test_bot.py`](https://github.com/karan/HackerNewsAPI/blob/master/my_test_bot.py)

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!

Tests
=====

To run the tests locally just install the requirements by running `pip install -r requirements.txt`.

Then run the command `nosetests -v` in the command line from within the projects root directory.

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/karan/hackernewsapi/trend.png)](https://bitdeli.com/free "Bitdeli Badge")