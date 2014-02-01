## v1.8.2 (Jan 31, 2014)

- New: Build stories from id (`Story.fromid(6115341)`)

## v1.8.1 (Jan 1, 2014)

- Fix: `IndexError` on `get_comments` - Issue #24
- Fix: Error on empty `td`

## v1.8.0 (Dec 27, 2013)

- Add: `get_stories()` is now a generator

## v1.7.2 (Dec 22, 2013)

- Add: `unittest` instead of `nose`
- Fix: Encoding errors

## v1.7.1 (Dec 17, 2013)

- Fix: `UnboundLocalError` on `num_comments`

## v1.7.0 (Dec 17, 2013)

- Add: Use `Story` class now instead of `dict`
- Add: Comment scraper (`story.get_comments()`)
- Fix: Python 3 compatibility
- Fix: `\xa0` encoding bug
- Remove: Python 2.6 compatibility

## v1.6.3

- Fix: Python 3 compatibility
- Fix: Unit tests to take into account HN throttling

## v1.6.2

- Add: Pagination
- Add: Python 3 compatibility
- Add: More test cases

## v1.6.1

- Add: Travis CI integration
- Add: Coveralls integration

## v1.6.0

- Add: Tests

## v1.5.9

- Fix: Publish time for job postings
- Fix: Versioning on PyPi
