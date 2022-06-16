#!/usr/bin/env python3
"""
vuz - command line tool to search univercities
Copyright (C) 2021-2022  usiqwerty

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#TODO:make dup-check
import requests, re
from time import sleep
from bs4 import BeautifulSoup
p=['█', '▓', '▒','░']

def deepscan(id, city):
	dict_vuzes=dict()
	result_vuzes=list()
	print(city)
	try:
		if city=='':
			url=f"https://vuzopedia.ru/program/bakispec/{id}/varianty"
		else:
			url=f"https://vuzopedia.ru/region/city/{city}/program/bakispec/{id}/varianty"
		print(f"{city} Deepscanning", id)
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
				result_vuzes.append(dict_vuzes[title])

	except requests.exceptions.ConnectionError:
		result_vuzes.append(-1)

	return(result_vuzes)

def vuzopedia(scores, city, theme, deep, hothead):
	page=1
	total=1
	current=0
	result_vuzes=list()
	vuzes=list()
	if hothead:
		print("HOTHEAD")
		citystr=''
	else:
		citystr=f"&city[]={city}"

	while current<total:
		msg=f'Processing: page {page} of {total} \t'
		print(msg+p[3]*round(80), end='\r')
		print(msg+p[0]*round(80*page/total), end='\r')

		url="https://vuzopedia.ru/vuzfilter/prog?vuz=&obshezh=&voenkaf=&budzh=&gosu=&theme={}&och=&zaoch=&ochzaoch=&distans=&vstupisp=&idcmb=&page={}&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}".format(theme, page, *scores)
		url+=citystr
		try:
			html=requests.get(url).text
			soup=BeautifulSoup(html, 'html.parser')
			vuz_list=soup.find_all("a", class_="spectittle")

			for i in vuz_list:
				id=re.findall( r"[0-9]+", i.get("href"))[0]
				ans= [ str(id), i.text.strip() ]
				if deep:
					scanned = deepscan(id, city if not hothead else '')
					if not scanned:
						continue
					ans += scanned
					#ans.append ( str(scanned) )
				result_vuzes.append(ans)

			if total==1:	#if we'll find out that it is really one, then
					#this loop won't run again,
					#because 'current' and 'total' would be equal
				pagination=soup.find("ul", class_="pagination")
				if pagination:
					pages=pagination.find_all("li")
					total=len(pages)

		except requests.exceptions.ConnectionError:
			result_vuzes.append(-1)
		page+=1
		current+=1
		if page%10==0:
			sleep(5)
		else:
			sleep(1)
	print("")
	return result_vuzes
