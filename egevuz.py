#!/usr/bin/env python3
import requests, re
from bs4 import BeautifulSoup

#IS IT REALLY NECESSARY???
#TODO: get rid of this
#
#def spbgu():
#	url="https://spbu.ru/postupayushchim/programms/bakalavriat?exam[10]={}&exam[11]={}&exam[212]={}&field[]=5".format(ru,math, inf)
#	resp=requests.get(url).text
#	pattern=r'js-crop-text">([\w\s;1-9\&,.]*)</[\w1-9]+>'
#	if resp.find("программ нет")>=1:
#		print ("Программ нет")
#	else:
#		mat=re.findall(pattern, resp)
#		for i in mat:
#			print(i.replace('&nbsp;', ' '))

result_vuzes=[]
def vuzopedia(marks, city):

	url="https://vuzopedia.ru/vuzfilter?vuz=&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}&city[]={}".format(*marks, city)
	print (url+"\n")
	print ("Подождите...", end='\r')
	try:
		html=requests.get(url).text
		soup=BeautifulSoup(html, 'html.parser')
		vuz_list=soup.find_all("div", class_="itemVuzTitle")

		for i in vuz_list:
			result_vuzes.append( i.text.strip() )
	except requests.exceptions.ConnectionError:
		return ( [], '' )

	return ( result_vuzes, url )
