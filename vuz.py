#!/usr/bin/env python3
import grades, egevuz, rsr
subjs=['Математика','Русский язык','Физика','Обществознание','История','Биология', 'Информатика', 'Химия', 'Литература', 'География', 'Иностранный язык']
cities={
	59:'Москва',
	50:'Санкт-Петербург',
	83:'Екатеринбург',
	5:'Архангельск',
	7:'Астрахань',
	76:'Владивосток',
	23:'Иваново',
	68:'Ростов-на-Дону',
	20:'Махачкала'
}

oly=False
advanced_olymps=False
city=0

#def main ():


if __name__=="__main__":
	print ("vuz rewritten v2.0")
	#print("testing 2.0")

#subjects
	for i in range(len(subjs)):
		print (str(i+1), "\t"+subjs[i])
	subjs_input=map( lambda x: int(x)-1 , input("Предметы через пробел: ").split(' ') )
	subs=list(subjs_input)
	print (subs)
	#subs=[0,1,6]
###

#cities
	for i in cities:
		print(i,"\t"+ cities[i])

	city=int(input("Код города: "))
	print(cities[city])
	olmps = True if input("Олимпиады y/n? ")=='y' else False
###

#EGE score
	grades=grades.get_grades(list(map(lambda x: subjs[x],subs)))
	for i in grades:
		#if i[:5].lower() in subjs
		try:
			curr=float(grades[i].replace(',','.'))
		except:
			continue
		grades[i]=round((curr-2)*33.3)
	print(grades)
###

#vuzopedia
	scores=[]
	for i in range(len(subjs)):
		score=''
		if subjs[i] in grades:
			score=str(grades[subjs[i]])
		scores.append(score)
	print(scores)
	url="https://vuzopedia.ru/vuzfilter?vuz=&mat={}&rus={}&fiz={}&obshe={}&ist={}&biol={}&inform={}&him={}&liter={}&georg={}&inyaz={}&city[]={}".format(*scores, city)
	vuzes=egevuz.vuzopedia(url)
	for i in vuzes:
		print(i)
###

#olympiads
	if olmps:
		olymps=set()
		for sub in filter(lambda x: int(scores[x])>=75, subs):
			print(subjs[sub])
			for i in rsr.olymps(False, subjs[sub].lower(), 1):
				olymps.add(i)
		for i in olymps:
			print(i)
###
