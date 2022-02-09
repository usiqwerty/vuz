#!/usr/bin/env python3
import csv, sys, requests
from os.path import join
from bs4 import BeautifulSoup
rsr_olymp=join("userdata", "rsr-olymp.csv")
def update():
	print ("Requesting rsr-olymp.ru...")
	html=requests.get("https://rsr-olymp.ru").text

	soup = BeautifulSoup(html, 'html.parser')
	table = soup.findAll("table")[1]
	rows = table.findAll('tr')

	total= len(rows)
	done=0

	with open(rsr_olymp, "w", newline='', encoding='utf8') as f:
		wr = csv.writer(f, delimiter=',', quotechar='"')

		for row in rows:
			row_text = []

			#it is possible to add 'th' to  findAll argument,
			#so you could iterate table header
			cols = row.findAll(['td'])
			for row_element in cols:
				row_text.append(row_element.text.replace('\n', '').strip())

			#if some cells were merged, we need to reserve place there
			times= 5 - len(row_text)
			row_text = [""]*times + row_text

			link=cols[1].find("a")
			row_text.append(link.get("href") if link else "")

			wr.writerow(row_text)

			done+=1
			print(f"Updating: {done}/{total}", end='\r')
	print("")


def olymps(subj, lvl):
	output=[]
	lastprintname=""

	with open(rsr_olymp, newline='', encoding='utf8') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd:
			#id=row[0]
			name=row[1]
			#theme=row[2]
			subject=row[3]
			level=row[4]
			link=row[5]
			if name!= "":
				#if this is next olympiad, not the continuation of last one
				lastname=name
				lastlink=link
			else:
				link=lastlink
				name=lastname
			if ( level==str(lvl) or lvl==0 ) and subj in subject:
				#if this is the one we need
				if lastprintname!=name:
					#and it wasn't printed before
					output.append(name+" "+link)
					lastprintname=name
	return output

if __name__=="__main__":
	args=sys.argv
	level=0
	subject=''
	result=[]

	for i in args:
		if i=="I":
			level=1
		elif i=="II":
			level=2
		elif i=="III":
			level=3
		elif i=="--update":
			update()
		elif i!= sys.argv[0]:
			subject=i
	#wrapper
	for i in olymps(subject, level):
		print(i)

