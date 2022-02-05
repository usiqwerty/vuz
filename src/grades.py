#!/usr/bin/env python3
import sys, csv
from . import tables

def get_average(subject):
	with open('grades.csv', newline='', encoding='utf8') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd: #iterate until subject was found, else return 0
			last=len(row)-1
			avg=row[last]	#avg value is in the last column
			if subject in row[0].lower():
				return avg.replace(',', '.')
				#we need to decimal delimeter to point
				#to make python able to convert string into float with 'float()' builtin
	return 0
def get_period(subject, period):
	with open('periods.csv', newline='', encoding='utf8') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd: #iterate until subject was found, else return 0
			col=period-1+2 #see the table
			avg=row[col]
			if subject in row[1].lower():
				return avg
	return 0

if __name__=="__main__":
	for i in range(len(sys.argv)):
		if sys.argv[i]=="--update":
			print("Running database update...")
			f=open('grades.xls')
			html=f.read()
			f.close()
			tables.html2csv('grades.xls', html)
