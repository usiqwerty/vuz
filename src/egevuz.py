#!/usr/bin/env python3
import requests, re
from bs4 import BeautifulSoup

result_vuzes=[]

def vuzopedia(marks, city):
	url="https://vuzopedia.ru/vuzfilter?vuz=&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}&city[]={}".format(*marks, city)

	try:
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'html.parser')
		vuz_list=soup.find_all("div", class_="itemVuzTitle")

		for i in vuz_list:
			result_vuzes.append( i.text.strip() )
	except requests.exceptions.ConnectionError:
		url=''

	return ( result_vuzes, url )
