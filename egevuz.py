#!/usr/bin/env python3

#TODO:make dup-check
import requests, re
from time import sleep
from bs4 import BeautifulSoup
p=['█', '▓', '▒','░']

def deepscan(id, city):
	#dict_vuzes=dict() #anti-dup
	result_vuzes=list()

	try:
		if city=='':
			url=f"https://vuzopedia.ru/program/bakispec/{id}/varianty"
		else:
			#print(f"City: {city}")
			url=f"https://vuzopedia.ru/region/city/{city}/program/bakispec/{id}/varianty"
		print(f"[{city}] Deepscanning", id)
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'html.parser')
		listed_vuzes=soup.find_all("a")
		if listed_vuzes:
			for i in listed_vuzes:
				title=i.find("div", class_="itemVuzTitle")
				if title:
					title=title.text.strip()
				else: #sus, maybe delete
					continue
				#if title not in dict_vuzes:
				#dict_vuzes[title]=re.findall(r"[0-9]+",i.get("href"))[0]

				result_vuzes.append(re.findall(r"[0-9]+",i.get("href"))[0]) #no anti-dup

	except requests.exceptions.ConnectionError:
		#result_vuzes.append(-1)
		return #None

	return(result_vuzes)

def vuzopedia(scores, city, theme, deep): #, hothead
	page=1 #for multi-page url
	#total=1	#maximum number of pages, it will be set later
	#current=0

	result_vuzes=list()
	#vuzes=list() kuk?
	if city=='':
		print("HOTHEAD")
		citystr=''
	else:
		citystr=f"&city[]={city}"

	while True:
		#msg=
		#print(msg+p[3]*round(80), end='\r')
		#print(msg+p[0]*round(80*page/total), end='\r') #super mega cool progressbar
		print(f'Processing: page {page}')

		url="https://vuzopedia.ru/vuzfilter/prog?vuz=&obshezh=&voenkaf=&budzh=&gosu=&theme={}&och=&zaoch=&ochzaoch=&distans=&vstupisp=&idcmb=&page={}&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}".format(theme, page, *scores)
		url+=citystr
		#print (url)
		try:
			html=requests.get(url).text
			soup=BeautifulSoup(html, 'html.parser')
			links_list=soup.find_all("a", class_="spectittle") #wait here's typo in classname, why does it work?!

			for i in links_list:
				id=re.findall( r"[0-9]+", i.get("href"))[0]
				ans= [ str(id), i.text.strip() ] #specid and spectitle
				if deep:
					scanned = deepscan(id, city) # if not hothead else ''
					if not scanned:
						continue
					ans += scanned #merge arrays
				result_vuzes.append(ans) #save to result

			#if total==1:	#if we'll find out that it is really one, then
					#we'd break out of the loop
			pagination=soup.find("ul", class_="pagination")
			if pagination:
				pages=pagination.find_all("li")
				if len(pages) <=3:
					break #last page
			else:
				print("No page links found, parsing stopped")
				break
				#if total==1:
				#	break


		except requests.exceptions.ConnectionError:
			####TODO: show results even on disconnect
			####result_vuzes.insert(0, -1)
			####break

			#just error, if something was found before loosing connection
			#we'd loose it
			return [-1] #return, since it's no need to iterate any further

		#current+=1
		page+=1
		if page%10==0:
			sleep(5)
		else:
			sleep(1)
	#print("")
	return result_vuzes
