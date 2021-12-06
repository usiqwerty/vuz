#!/usr/bin/env python3
import csv, sys, requests, tables
import pandas as pd
from bs4 import BeautifulSoup




def walkthrough(upd, subj, lvl):
	output=list()
	lastprintname=""
	if upd:
		print ("Fetching data...")
		html=requests.get("https://rsr-olymp.ru").text
		tables.html2csv('rsr-olymp.csv', html)
	with open('rsr-olymp.csv', newline='') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd:
			id=row[0]
			name=row[1]
			theme=row[2]
			subject=row[3]
			level=row[4]
			if name!= "":
				lastname=name
			else:
				name=lastname
			if ( level==str(lvl) or lvl==0 )and subject.find(subj)>=0:
				if lastprintname!=name:
					output.append(name)
					#print (name)
					lastprintname=name
	return output
#def get(lvl=0,subj='',upd=False):

if __name__=="__main__":
	args=sys.argv
	level=0 #default
	subject=''
	result=list()

	upd=False
	for i in args:
		if i=="I":
			level=1
		elif i=="II":
			level=2
		elif i=="III":
			level=3
		elif i!="--update" and i!='' and i!= sys.argv[0]:
			subject=i
		elif i=="--update":
			upd=True
	for i in walkthrough(upd, subject, level):
		print(i)

