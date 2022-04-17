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

import csv, sys
from os.path import join
from bs4 import BeautifulSoup
grades_csv=join("userdata","grades.csv")
grades_html=join("userdata","grades.html")
def update():
	f=open(grades_html)
	html=f.read()
	f.close()

	soup = BeautifulSoup(html, 'html.parser')
	table=soup.findAll("table")[1] #we're taking only second table in .html file
	rows = table.findAll('tr')

	with open(grades_csv, "w", newline='', encoding='utf8') as f:
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
	with open(grades_csv, newline='') as file:
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
