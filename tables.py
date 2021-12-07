#!/usr/bin/env python3
import csv, sys, requests
import pandas as pd
from bs4 import BeautifulSoup

args=sys.argv
def html2csv(filename, html):
	basename=filename.split('.')[0]
	#print ("Reading data...  [   ]", end='\r')

	print ("Processing...    [*  ]", end='\r')
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.findAll("table")[1]
	rows = table.findAll('tr')

	row_text_array = []
	for row in rows:
		row_text = []
		#it is possible to add 'th' to  findAll argument,
		#so you could iterate table header
		for row_element in row.findAll(['td']):
			row_text.append(row_element.text.replace('\n', '').strip())

		#if some cells were merged, we need to reserve place there

		#TODO: get rid of loop-based row extender
		for i in range ( 5 - len(row_text) ):
			row_text.insert(0, "")
		row_text_array.append(row_text)

	print ("Saving...        [** ]", end='\r')
	with open(basename+".csv", "w", newline='', encoding='utf8') as f:
		wr = csv.writer(f, delimiter=',', quotechar='"')
		for row_text_single in row_text_array:
			wr.writerow(row_text_single)
	print ("Database updated [***]")

if __name__=="__main__":
	if len(sys.argv)==2:
		html2csv(sys.argv[1])
	else:
		html2csv(input(".html to be converted to .csv: "))
