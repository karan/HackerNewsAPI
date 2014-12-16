![Hacker News API](https://raw.github.com/karan/HackerNewsAPI/master/HN.jpg)

Unofficial Python API for [Hacker News](https://news.ycombinator.com/).


| Build Status | Test Coverage | Version | Downloads |
| ------------ | ------------- | ------- | ------------------- |
| [![Build Status](https://travis-ci.org/karan/HackerNewsAPI.png?branch=master)](https://travis-ci.org/karan/HackerNewsAPI) | [![Coverage Status](https://coveralls.io/repos/karan/HackerNewsAPI/badge.png)](https://coveralls.io/r/karan/HackerNewsAPI) | [![Latest Version](https://pypip.in/v/HackerNews/badge.png)](https://pypi.python.org/pypi/HackerNews/) | [![Downloads](https://pypip.in/d/HackerNews/badge.png)](https://pypi.python.org/pypi/HackerNews/) |


Features
========

- Compatible with Python 2 (2.7+).
- Supports 'top', 'news2','newest' and 'best' posts
- Retrieve comments from posts (flat list for now) (`story.get_comments()`)
- Pagination support for comments
- Handles external posts, self posts and job posts
- Get post details for any post (`Story.fromid(7024626)`)


Installation
========

    $ pip install HackerNews


Usage
========

**NOTE:** Do not make a lot of requests in a short period of time. HN has it's own throttling system.


    from hn import HN

    hn = HN()

    # print the first 2 pages of newest stories
    for story in hn.get_stories(story_type='newest', limit=60):
        print(story.rank, story.title)


API Reference
========

## Class: `HN`

### Get stories from Hacker News

#### `get_stories`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `story_type` | string | No | Returns the stories from this page. One of `(empty string)`, `news2`, `newest`, `best` | `(empty string)` (top) |
| `limit` | integer | No | Number of stories required from the given page. Cannot be more than 30. | 30 |

**Example:**

	from hn import HN
	hn = HN()
	hn.get_stories(story_type='newest', limit=10)

#### `get_leaders`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `limit` | integer | No | Number of top leaders to return | 10 |

**Example:**

    from hn import HN
    hn = HN()

    # get top 20 users of HN
    hn.get_leaders(limit=20)

## Class: `Story`

Each `Story` has the following properties

- **rank** - the rank of story on the page (keep pagination in mind)
- **story_id** - the story's id
- **title** - the title of the story
- **is_self** - true for self/job stories
- **link** - the URL it points to (`''` for self posts)
- **domain** - the domain of the link (`''` for self posts)
- **points** - the points/karma on the story
- **submitter** - the user who submitted the story (`''` for job posts)
- **submitter_profile** - the above user's profile link (can be `''`)
- **published_time** - the published time
- **num_comments** - the number of comments a story has
- **comments_link** - the link to the comments page

### Make an object from the ID of a story

#### `fromid`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `item_id` | integer | Yes | Initializes an instance of Story for given item_id. Must be a valid story id. |  |

**Example:**

	from hn import Story
	story = Story.fromid(6374031)
	print story.title

### Get a list of Comment's for this story

#### `get_comments`

**Parameters:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
|  |  |  |  |  |

**Example:**

	from hn import Story
	story = Story.fromid(6374031)
	comments = story.get_comments()

## Class: `Comment`

Each `Comment` has the following properties

- **comment_id** - the comment's item id
- **level** - comment's nesting level
- **user** - user's name who submitted the post
- **time_ago** - time when it was submitted
- **body** - text representation of comment (unformatted)
- **body_html** - html of comment, may not be valid

## Class: `User`

Each `User` has the following properties

- **username** - user's profile name
- **date_created** - when the profile was created
- **karma** - user's e-points
- **avg** - user's average karma per day

Examples
========

See [`my_test_bot.py`](https://github.com/karan/HackerNewsAPI/blob/master/my_test_bot.py)


Tests
========

To run the tests locally just do:

    $ chmod 777 runtests.sh
    $ ./runtests.sh

To run individual tests,

    $ python -m unittest tests.<module name>

The tests are run on a local test server with predownloaded original responses.

Donations
========

If HackerNewsAPI has helped you in any way, and you'd like to help the developer, please consider donating.

**- BTC: [19dLDL4ax7xRmMiGDAbkizh6WA6Yei2zP5](http://i.imgur.com/bAQgKLN.png)**

**- Flattr: [https://flattr.com/profile/thekarangoel](https://flattr.com/profile/thekarangoel)**


Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
