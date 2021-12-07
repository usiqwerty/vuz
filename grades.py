#!/usr/bin/env python3
import sys, tables, csv

def get_average(subject):
	with open('grades.csv', newline='', encoding='utf8') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd: #iterate until subject was found, else return 0
			last=len(row)-1
			avg=row[last]
			if row[0].lower().find(subject)>=0:
				return avg.replace(',', '.')
				#we need to decimal delimeter to point
				#to make python able to convert string into float
	return 0

if __name__=="__main__":
	for i in range(len(sys.argv)):
		if sys.argv[i]=="--update":
			print("Running database update...")
			f=open('grades.xls')
			html=f.read()
			f.close()
			tables.html2csv('grades.xls', html)
