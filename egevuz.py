#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup



def vuzopedia(url):
	result_vuzes=[]
	try:
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'html.parser')
		vuz_list=soup.find_all("div", class_="itemVuzTitle")

		for i in vuz_list:
			result_vuzes.append( i.text.strip() )
	except requests.exceptions.ConnectionError:
		result_vuzes.append(-1)

	return result_vuzes
