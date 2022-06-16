#!/usr/bin/env python3
'''
inputs=[
	"рыжий лис",
	"рыжий мальчик",
	"весёлый мальчик"
]
'''
import csv

def gentree(phrases):
	ph_split=[]
	words=set()
	tree={}

	for phrase in phrases:
		ph_split.append(phrase.split())
	#for phrase in ph_split:
	#	print(phrase)

	for phrase in ph_split:
		words.add(phrase[0])

	for phrase in ph_split:
		key=phrase[0]
		if key in words:
			sus=True
		else:
			sus=False

		if sus:
			if key in tree:
				tree[key]+=[phrase[1:]]
			else:
				tree[key]=[phrase[1:]]
	return tree
def showtree(tree):
	for key in tree:
		print(key)
		for entry in tree[key]:
			print('\t', entry)
		print()
if __name__=="__main__":
	vzs=[]
	with open("userdata/vuzes.csv", "r", newline="", encoding="utf8") as f:
		rd=csv.reader(f, delimiter=",", quotechar='"')
		for row in rd:
			vzs.append(row[1])

	tr=gentree(vzs)
	showtree(tr)
