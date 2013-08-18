#!/usr/bin/env python

from hn import HN

hn = HN()

for story in hn.get_top_stories()[:5]:
    print story.print_story()
    print '*' * 40
    print ''