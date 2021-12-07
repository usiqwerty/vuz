#!/usr/bin/env python3
import requests, re
from bs4 import BeautifulSoup
ru=60
math=60
inf=60

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

def vuzopedia(marks, city):
	#TODO: is it really necesary to convert these?
	mat=marks[0]
	rus=marks[1]
	fiz=marks[2]
	obshe=marks[3]
	ist=marks[4]
	biol=marks[5]
	inform=marks[6]
	him=marks[7]
	liter=marks[8]
	georg=marks[9]
	inyaz=marks[10]
	url="https://vuzopedia.ru/vuzfilter?vuz=&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}&city[]={}".format(mat,rus,fiz,obshe,ist,biol,inform,him,liter,georg,inyaz,city)
	print (url)
	html=requests.get(url).text
	soup=BeautifulSoup(html, 'html.parser')
	vuz_list=soup.find_all("div", class_="itemVuzTitle")

	for i in vuz_list:
		print(i.text.strip())


def ege(marks, city=1):
	vuzopedia(marks, city)
#test
#ege(mat=60,rus=60,inform=60)
