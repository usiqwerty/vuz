#!/usr/bin/env python3
import requests, sys
import rsr
import pandas as pd
from bs4 import BeautifulSoup
url="https://info.olimpiada.ru/events/count/2500?class[10]=on"

def olymp_dates():
	result=[]
	print(url)
	#html=requests.get(url).text
	with open('tmp.html', 'r') as f:
		html=f.read()
	soup=BeautifulSoup(html, 'html.parser')
	list_in_div=soup.find_all("div", class_="inner_main")[0]
	rows=list_in_div.find_all("table")

	date="00.00"
	for i in rows:
		date_tag=i.find("span", class_="event_date")
		if date_tag:
			date=date_tag.text
		title=i.find("a").text
		result.append( (date[2:], title) )
	return result
def compare(upd, subj, lvl):
	dts=[]
	olmps=[]
	for date, name in olymp_dates():
		dts.append(date)
		olmps.append(name)

	result=[]
	id=0
	for i in rsr.olymps(upd, subj, lvl):
		for j in olmps:
			if i.lower() in j.lower():
				result.append( (dts[olmps.index(j)], i ) )

		id+=1
	return result
if __name__=="__main__":
	args=sys.argv
	level=0
	subject=''
	result=[]

	upd=False
	for i in args:
		if i=="I":
			level=1
		elif i=="II":
			level=2
		elif i=="III":
			level=3
		elif i=="--update":
			upd=True
		elif i!= sys.argv[0]:
			subject=i


	for date,name in compare(upd,subject, level):
		print(date, name)
