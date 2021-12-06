#!/usr/bin/env python3
import sys, tables, csv

if __name__=="__main__":
	for i in range(len(sys.argv)):
		if sys.argv[i]=="--update":
			print("Running database update...")
			f=open('sgo.xls')
			html=f.read()
			f.close()
			tables.html2csv('sgo.xls', html)

def get_average(subject):
	with open('sgo.csv', newline='') as csvfile:
		rd=csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in rd:
			last=len(row)-1
			avg=row[last]
			if row[0].lower().find(subject)>=0:
				#print(subject, row[0], avg)
				return avg.replace(',', '.')
	return 0
