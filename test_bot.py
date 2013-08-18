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