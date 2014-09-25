# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json


def get_info(parrafo):
 	print parrafo.split('-')[0].strip()



session = requests.Session()

# First
response = session.get('http://localhost:8000')
soup = BeautifulSoup(response.text)

csrftoken = response.cookies['csrftoken']

parrafo = soup.find('p').getText()
get_info(parrafo)

# AJAX requests
for page in xrange(2, 11):
	headers = {
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'X-CSRFToken': csrftoken,
	}
	data = {'page': page}
	response = session.post('http://localhost:8000/more/', data=data, headers=headers)
	data = response.json()
	get_info(data['parrafo'])
