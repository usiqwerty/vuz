#!/usr/bin/env python3
import marks, sys, grades


if __name__=="__main__":

	m=input("m: ").split(" ")
	r=[]
	for i in m:
		r.append(int(i))

	avg, rise, deg = marks.calculate(r)
	if rise[0]!=-1:
		fives, fofi, fofifi= rise
		print (fives)
	else:
		print("Already five")
