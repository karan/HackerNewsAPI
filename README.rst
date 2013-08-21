.. figure:: https://raw.github.com/thekarangoel/HackerNewsAPI/master/HN.jpg
   :alt: Hacker News API

   Hacker News API
Unofficial Python API for `Hacker
News <https://news.ycombinator.com/>`__. Currently supports reading HN
homepage and newest stories page only.

Installation
============

::

    $ pip install HackerNews

Dependencies
============

**Beautiful Soup**

::

    $ pip install beautifulsoup4

Classes
=======

``HN``
------

The class that parses the HN page, and builds up all Story objects

Methods
^^^^^^^

``get_top_stories()`` - Returns a list of Story objects from the
homepage of HN

``get_newest_stories()`` - Returns a list of Story objects from the
newest page of HN

``Story``
---------

Story class represents one single story on HN

Methods
^^^^^^^

``print_story()`` - Print the details of a story

Story details
^^^^^^^^^^^^^

-  **rank** - the rank of story on the page
-  **story\_id** - the story's id
-  **title** - the title of the story
-  **is\_self\_post** - true for self/job stories
-  **link** - the url it points to (None for self posts)
-  **domain** - the domain of the link (None for self posts)
-  **points** - the points/karma on the story
-  **submitter** - the user who submitted the story
-  **submitter\_link** - the above user profile link
-  **published\_time** - the published time ago
-  **num\_comments** - the number of comments it has
-  **comments\_link** - the link to the comments page

Example
=======

```test_bot.py`` <https://github.com/thekarangoel/HackerNewsAPI/blob/master/test_bot.py>`__
prints top and new posts.

::

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
        

Contribute
==========

If you want to add any new features, or improve existing ones, feel free
to send a pull request!
