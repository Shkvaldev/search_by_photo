# -*- coding: utf-8 -*-
import requests as r
from bs4 import BeautifulSoup
import json
from config import SOCIAL_NETWORKS, SOCIAL_NETWORKS_NAMES
import re

def create_file_url(file):
	data = open(file, 'rb').read()
	file_url = r.post('https://yandex.ru/images-apphost/image-download', data=data)
	return json.loads(file_url.text)

def get_page(file_url):
	params = {
		'url': file_url['url'],
		'rpt': 'imageview'
	}
	page = r.get('https://yandex.ru/images/search', params=params)
	return page.text

def get_mentions(page):
	links = list()
	soup = BeautifulSoup(page, 'html.parser')
	for link in soup.select("a.Link.Link_theme_outer"):
		links.append(link['href'])
	return links

def sort_social_networks(links):
	results = list()
	for i in range(len(links)):
		for j in range(len(SOCIAL_NETWORKS)):
			if len(re.findall(SOCIAL_NETWORKS[j], links[i])) > 0:
				results.append(SOCIAL_NETWORKS_NAMES[j]+": "+links[i])
	return results

def yandex_photo_search_bundle(file): # Возвращает список формата [[упоминания], [соцсети]]
	result = list()
	file = create_file_url(file)
	page = get_page(file)
	mentions = get_mentions(page)
	if len(mentions) > 0:
		result.append(mentions)
		sn = sort_social_networks(mentions)
		result.append(sn) 
		return result
	else:
		return result.append(list())