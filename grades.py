#!/usr/bin/env python3
import csv
def get_grades(subs):
	result=dict()
	with open('grades.csv', newline='') as file:
		rd=csv.reader(file, delimiter=",", quotechar='"')
		for row in rd:
			for i in subs:
				if i in row[0]:
					result[row[0]]=row[len(row)-1]
	return result
