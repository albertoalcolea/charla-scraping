# -*- coding: utf-8 -*-
import requests

BASE_URL = 'http://opendata.aragon.es/socialdata'

ENDPOINT_TRENDINGS = BASE_URL + '/trendings'
ENDPOINT_DATA = BASE_URL + '/data'


def get_top_50_trends():
	""" 
	Obtiene las 50 tendencias diferenciales de Aragón.
	http://opendata.aragon.es/socialdata/trendings?type=diff
	"""
	url = ENDPOINT_TRENDINGS + '?type=diff'
	resp = requests.get(url)
	trends = resp.json()
	for trend in trends['results']:
		print trend['name']


def get_data_from_twitter():
	"""
	Obtiene las 20 primeras páginas de resultados de twitter usando paginación estándar.
	Imprime el autor de cada tweet.
	http://opendata.aragon.es/socialdata/data?source=twitter&page=p
	"""
	url = ENDPOINT_DATA + '?source=twitter&page={0}'
	MAX_PAGE = 20
	for p in xrange(1, MAX_PAGE+1):
		resp = requests.get(url.format(p))
		data = resp.json()
		for tweet in data['results']:
			print tweet['author']


def example_pagination_by_id():
	"""
	Obtiene las 20 primeras páginas de twitter usando paginación por id.
	Imprime el autor de cada tweet.
	http://opendata.aragon.es/socialdata/data?source=twitter&since_id=x&max_id=y
	"""
	url = ENDPOINT_DATA + '?source=twitter&since_id={0}&max_id={1}'
	min_id = 600
	last_id = 1000

	while last_id > min_id:
		resp = requests.get(url.format(min_id, last_id))
		data = resp.json()
		for tweet in data['results']:
			print tweet['author'], tweet['id']
		ids = [res['id'] for res in data['results']]
		last_id = min(ids)


def get_geo_center():
	"""
	Obtiene resultados publicados en un radio de 10 km alrededor de las coordenadas dadas.
	Imprime las coordenadas de los resultados de la primera página.
	http://opendata.aragon.es/socialdata/data?center=lat,lng&distance=km
	"""
	url = ENDPOINT_DATA + '?center={0},{1}&distance={2}'
	lat = 41.35678
	lng = -0.8148576
	radio = 10 # Km
	resp = requests.get(url.format(lat, lng, radio))
	data = resp.json()
	for res in data['results']:
		print res['lat'], ',', res['lng']


def get_geo_bounding_box():
	"""
	Obtiene resultados publicados en dentro de un bounding box "rectángulo geométrico"


	max_lat, min_lng -> |------------------| <- max_lat, max_lng
                        |                  |
                        |                  |
                        |                  |
	min_lat, min_lng -> |------------------| <- min_lat, max_lng


	Imprime las coordenadas de los resultados de la primera página.
	http://opendata.aragon.es/socialdata/data?bbox=min_lng,min_lat,max_lng,max_lat
	"""
	url = ENDPOINT_DATA + '?bbox={0},{1},{2},{3}'
	min_lat = 41.35678
	max_lat = 41.78553
	min_lng = -0.8148576
	max_lng = -0.667584

	"""
	41.78, -0.814 -> |------------------| <- 41.78, -0.667
                     |                  |
                     |                  |
                     |                  |
	41.35, -0.814 -> |------------------| <- 41.35, -0.667
	"""

	resp = requests.get(url.format(min_lng, min_lat, max_lng, max_lat))
	data = resp.json()
	for res in data['results']:
		print res['lat'], ',', res['lng']


def get_geo_locality():
	"""
	Obtiene resultados publicados en un radio de 10 km alrededor de un municipio.
	Imprime las coordenadas de los resultados de la primera página.
	http://opendata.aragon.es/socialdata/data?locality=locality&distance=distance_in_km
	"""
	url = ENDPOINT_DATA + '?locality={0}&distance={1}'
	locality = 'jaca'
	radio = 10 # Km
	resp = requests.get(url.format(locality, radio))
	data = resp.json()
	for res in data['results']:
		print res['lat'], ',', res['lng']


def filter_by_time_frame():
	"""
	Obtiene resultados publicados en un periodo de tiempo.
	Imprime la fecha de publicación de los resultados de la primera página
	http://opendata.aragon.es/socialdata/data?start_date=x&end_date=y
	"""
	url = ENDPOINT_DATA + '?start_date={0}&end_date={1}'
	start_date = '15/9/2014'
	end_date = '18/9/2014'
	resp = requests.get(url.format(start_date, end_date))
	data = resp.json()
	for res in data['results']:
		print res['published_on']


if __name__ == '__main__':
	get_top_50_trends()
	#get_data_from_twitter()
	#example_pagination_by_id()
	#get_geo_center()
	#get_geo_bounding_box()
	#get_geo_locality()
	#filter_by_time_frame()
