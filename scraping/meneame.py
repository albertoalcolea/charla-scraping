# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

BASE_URL = 'http://www.meneame.net/search?q={0}&page={1}'

KEYWORDS = [
	'aragón',
	# 'zaragoza',
	# 'huesca',
	# 'teruel',
	# 'jaca',
	# 'jacathon',
	# '...',
]

DELAY = 0.1


def haz_algo(title, description, author):
	print 'Titulo:', title
	print 'Autor:', author
	print
	print 'Descripción'
	print description
	print
	print '-------------------------------------------'
	print


def process_entry(entry):
	title = entry.find('h2').getText().strip()
	description = entry.find('div', class_='news-details').previous_sibling.strip()
	author = entry.find('div', class_='news-submitted').find_all('a')[1].getText()
	haz_algo(title, description, author)


def run():
	for keyword in KEYWORDS:

		page = 1
		morePages = True

		while morePages:
			url = BASE_URL.format(keyword, page)

			# Raw response
			response = requests.get(url)

			# Syntax tree
			soup = BeautifulSoup(response.text)

			entries = soup.find_all('div', class_='news-summary')

			if len(entries) == 0:
				morePages = False
				print 'Ultima pagina:', page
			else:
				for entry in entries:
					process_entry(entry)
				page += 1
				time.sleep(DELAY)
				


if __name__ == '__main__':
	run()
