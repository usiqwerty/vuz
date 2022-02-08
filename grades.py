#!/usr/bin/env python3
import csv, sys
from bs4 import BeautifulSoup

def update():
	f=open("grades.html")
	html=f.read()
	f.close()

	soup = BeautifulSoup(html, 'html.parser')
	table = soup.findAll("table")[1]
	rows = table.findAll('tr')

	with open("grades.csv", "w", newline='', encoding='utf8') as f:
		wr = csv.writer(f, delimiter=',', quotechar='"')

		for row in rows:
			row_text = []
			cols = row.findAll('td')
			for row_element in cols:
				row_text.append(row_element.text.replace('\n', '').strip())
			if not row_text:
				continue
			wr.writerow(row_text)

def get_grades(subs):
	result=dict()
	with open('grades.csv', newline='') as file:
		rd=csv.reader(file, delimiter=",", quotechar='"')
		for row in rd:
			for i in subs:
				if i in row[0]:
					result[row[0]]=row[len(row)-1]
	return result
if __name__=="__main__":
	for i in sys.argv:
		if i=="--update":
			update()
