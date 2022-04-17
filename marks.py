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

def test(sum, count):
	result=[]

	test=0

	s=sum
	c=count
	adv=0

	if s/c>=4.5:
		result=[-1]
		return result
	while test<4.5:
		s+=5
		adv+=1
		test=s/(c+adv)
		if adv>7:
			adv=-1
			break
	result.append(adv)

	s=sum
	c=count
	adv=0
	while test<4.5:
		s+=4+5
		adv+=2
		test=s/(c+adv)
		if adv>14:
			adv=-1
			break
	result.append(adv)

	s=sum
	c=count
	adv=0
	while test<4.5:
		s+=4+5+5
		adv+=3
		test=s/(c+adv)
		if adv>21:
			adv=-1
			break
	result.append(adv)
	return result
def deg_test(sum, count):
	result=[]
	test=0
	for i in [2, 3, 4]:
		s=sum
		c=count
		test=s/c
		adv=0
		while test>=4.5:
			s+=i
			adv+=1
			test=s/(c+adv)
		result.append(adv)
	return result
def calculate(marks):
	count_init=0
	sum_init=0
	for j in marks:
		sum_init+=j
		count_init+=1
	avg=sum_init/count_init
	rise=test(sum_init, count_init)
	degrade=deg_test(sum_init, count_init)
	return (avg, rise, degrade)

if __name__=="__main__":
	print ("Marks perspective calculator by usiqwerty")
	i=input()
	count_init=0
	sum_init=0
	for j in i.split(" "):
		sum_init+=int(j)
		count_init+=1
	rise=test(sum_init, count_init)
	print ( "Current average: {} with {} marks".format(sum_init/count_init, count_init) )
	print("===")
	if rise[0]==-1:
		print("Already five")
	else:
		print("Fives: {}\nFour-fives: {}\nFour-five-fives: {}".format(*rise))
	print("===")
	degrade=deg_test(sum_init, count_init)
	print("Twos: {}\nThrees: {}\nFours: {}".format(*degrade))
