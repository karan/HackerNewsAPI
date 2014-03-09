#!/usr/bin/env python
from constants import BASE_URL
from utils import get_soup, get_item_soup

# https://news.ycombinator.com/leaders
def hackernews_leaders(limit=10):
	""" Return the leaders of Hacker News """
	if limit == None:
		limit = 10
	soup = get_soup('leaders')
	table = soup.find('table')
	leaders_table = table.find_all('table')[1]
	listLeaders = leaders_table.find_all('tr')[2:]
	listLeaders.pop(10) # Removing because empty in the Leaders page
	result = []
	for i, leader in enumerate(listLeaders):
		if (i == limit): 
			return result
		if not leader.text == '':
			item = leader.find_all('td')
			result.append([item[0].text, item[1].text, item[2].text, item[3].text])