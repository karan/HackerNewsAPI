#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

from .constants import BASE_URL, INTERVAL_BETWEEN_REQUESTS

def get_soup(page=''):
    """
    Returns a bs4 object of the page requested
    """
    content = requests.get('%s/%s' % (BASE_URL, page)).text
    return BeautifulSoup(content)

def get_item_soup(story_id):
    """
    Returns a bs4 object of the requested story
    """
    content = requests.get('%s/item?id=%s' % (BASE_URL, str(story_id))).text
    return BeautifulSoup(content)