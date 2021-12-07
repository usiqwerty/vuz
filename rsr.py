#!/usr/bin/env python3
import csv, sys, requests, tables
import pandas as pd
from bs4 import BeautifulSoup




def olymps(upd, subj, lvl):
	output=[]
	lastprintname=""
	if upd:
		print ("Fetching data...")
		html=requests.get("https://rsr-olymp.ru").text
		tables.html2csv('rsr-olymp.csv', html)
	with open('rsr-olymp.csv', newline='', encoding='utf8') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd:
			#id=row[0]
			name=row[1]
			#theme=row[2]
			subject=row[3]
			level=row[4]

			if name!= "":
				#if this is next olympiad
				lastname=name
			else:
				name=lastname
			if ( level==str(lvl) or lvl==0 ) and subj in subject:
				#if this is the one we need

				if lastprintname!=name:
					#and it wasn't printed before
					output.append(name)
					lastprintname=name
	return output

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

	#standalone wrapper
	for i in olymps(upd, subject, level):
		print(i)

