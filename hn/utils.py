#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

from .constants import BASE_URL, INTERVAL_BETWEEN_REQUESTS

def get_soup(self, page=''):
    """
    Returns a bs4 object of the page requested
    """
    content = requests.get('%s/%s' % (BASE_URL, page)).text
    return BeautifulSoup(content)