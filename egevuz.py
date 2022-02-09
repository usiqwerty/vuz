#!/usr/bin/env python3
import requests, re
from time import sleep
from bs4 import BeautifulSoup
p=['█', '▓', '▒','░']
dict_vuzes=dict()

def deepscan(id):
	result_vuzes=set()
	try:
		url=f"https://vuzopedia.ru/program/bakispec/{id}/varianty"
		print("Deepscanning", id)
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'html.parser')
		listed_vuzes=soup.find_all("a")
		if listed_vuzes:
			for i in listed_vuzes:
				title=i.find("div", class_="itemVuzTitle")
				if title:
					title=title.text.strip()
				else:
					continue
				if title not in dict_vuzes:
					dict_vuzes[title]=re.findall(r"[0-9]+",i.get("href"))[0]
				result_vuzes.add(dict_vuzes[title])


	except requests.exceptions.ConnectionError:
		result_vuzes.add(-1)

	return(result_vuzes)

def vuzopedia(scores, city, theme, deep):
	page=1
	total=1
	current=0
	result_vuzes=set()
	vuzes=set()

	while current<total:
		msg=f'Processing: {page}/{total} \t'
		print(msg+p[3]*round(80), end='\r')
		print(msg+p[0]*round(80*page/total), end='\r')

		print(f"Fetching data... Pass {page} of {total}", end='\r')
		url="https://vuzopedia.ru/vuzfilter/prog?vuz=&obshezh=&voenkaf=&budzh=&gosu=&theme={}&och=&zaoch=&ochzaoch=&distans=&vstupisp=&idcmb=&page={}&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}&city[]={}".format(theme, page, *scores, city)
		try:
			html=requests.get(url).text
			soup=BeautifulSoup(html, 'html.parser')
			vuz_list=soup.find_all("a", class_="spectittle")

			for i in vuz_list:
				id=re.findall( r"[0-9]+", i.get("href"))[0]
				ans= str(id) + " "+ i.text.strip()
				if deep:
					ans += " " + str(deepscan(id))
				result_vuzes.add(ans)


			if total==1:	#if we'll find out that it is really one, then
					#this loop won't run again,
					#because 'current' and 'total' would be equal
				pagination=soup.find("ul", class_="pagination")
				if pagination:
					pages=pagination.find_all("li")
					total=len(pages)


		except requests.exceptions.ConnectionError:
			result_vuzes.add(-1)
		page+=1
		current+=1
		if page%10==0:
			sleep(3)
		else:
			sleep(1)
	print("")
	return list(result_vuzes)
