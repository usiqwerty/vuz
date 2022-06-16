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

import sys, os, csv
import grades, egevuz, rsr, printer, wordgroup
version="volk ubil zaitsa v4.0dev"
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
themes={
1: "Управление и менеджмент",
2: "Экономика и финансы",
3: "Математика, информационные науки и технологии",
4: "Образование и педагогика",
5: "Искусство и культура",
6: "Машиностроение, автоматизация и робототехника",
7: "Транспорт: наземный, воздушный, водный",
8: "Строительство, архитектура и недвижимость",
9: "Юриспруденция",
10: "Химико-биологические науки и технологии",
11: "Науки о земле, геология и геодезия",
12: "Энергетика и электротехника",
13: "Филология и лингвистика",
14: "Экология, природообустройство и безопасность",
15: "СМИ, журналистика, реклама и PR",
16: "Психология",
17: "Электроника, связь и радиотехника",
18: "Сельское, лесное и рыбное хозяйство",
19: "Сервис, туризм и гостиничное дело",
20: "Дизайн",
21: "Физико-технические науки и технологии",
22: "Технологии легкой и пищевой промышленности",
23: "Технологические машины, оборудование и спецтранспорт",
24: "Медицина и здравоохранение",
25: "Качество и управление в технических системах",
26: "Логистика",
27: "Политика и международные отношения",
28: "Торговля и товароведение",
29: "Управление персоналом",
30: "История, археология и документоведение",
31: "Социология и социальная работа",
32: "Физическая культура, спорт и фитнес",
33: "Технологии материалов и металлургия",
34: "Маркетинг",
35: "Приборостроение, оптика и биотехника",
36: "Оружие и системы вооружения",
37: "Философия и религия",
38: "Нанотехнологии и наноматериалы"}
if __name__=="__main__":
	print("Copyright (C) 2021-2022 usiqwerty")
	print("This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE file")
	print("This is free software, and you are welcome to redistribute it")
	print("under certain conditions; see LICENSE for details.")


	city=0
	printout=False
	deep=False
	hothead=False
	verbose_vuzes=False
	for i in sys.argv:
		try:
			city=int(i)
		except:
			if i=="--update":
				rsr.update()
			elif i=="--print":
				printout=True
			elif i=="--deep":
				deep=True
			elif i=="--verbose":
				verbose_vuzes=True
			elif i=="--hothead":
				hothead=True
			elif i=="--help":
				print()
				print(f"{sys.argv[0]} [city_id] [--update] [--print] [--deep] [--verbose]")
				quit()
			continue
	print ("vuz", version)

#subjects
	for i in range(len(subjs)):
		print (str(i+1), "\t"+subjs[i])
	subjs_input=map( lambda x: int(x)-1 , input("Предметы через пробел: ").split(' ') )
	subs=list(subjs_input)
	#subs=[0,1,6]
###

#cities
	if city==0:
		for i in cities:
			print(i,"\t"+ cities[i])
		city=int(input("Код города: "))
		print(cities[city])
	#city=83
###
	olmps = True if input("Олимпиады y/n? ")=='y' else False
	#olmps=True


#EGE score
	grades=grades.get_grades(list(map(lambda x: subjs[x],subs)))
	for i in grades:
		try:
			curr=float(grades[i].replace(',','.'))
		except:
			continue
		grades[i]=round((curr-2)*33.3)
###
#themes
	for i in themes:
		print(i,"\t"+ themes[i])
	theme=int(input("Тематика: "))
	print(themes[theme])
###
	if printout and not deep and not verbose_vuzes:
		verbose_vuzes = True if input("Прописать названия вузов в дополнение к их номерам y/n? ")=="y" else False
#vuzopedia
	scores=[]
	for i in range(len(subjs)):
		score=''
		if subjs[i] in grades:
			score=str(grades[subjs[i]])
		scores.append(score)
	#scores=['80', '80', '', '', '', '', '80', '', '', '', '']
	#print(scores)
	vuzes=egevuz.vuzopedia(scores, city, theme, deep, hothead)
	string_vuzes = list(map(' '.join, vuzes))
	for i in vuzes:
		if i==-1:
			print("Нет интернета")
			quit()
		#print(i) wordgroup will do it
###
	print("https://vuzopedia.ru/program/bakispec/<id>")
#olympiads
	if olmps:
		olymps=set()
		for sub in filter(lambda x: int(scores[x])>=75, subs):
			for i in rsr.olymps(subjs[sub].lower(), 1):
				olymps.add(i)
		for i in olymps:
			print(i)
	else:
		olymps=['Поиск олимпиад не производился']
	if printout:
		print("Generating printout...")
		if hothead:
			city=''
		else:
			city=cities[city]
		printer.printout(string_vuzes, olymps, list(filter(lambda x: x!='', scores)), version, egevuz.dict_vuzes, verbose_vuzes, city)
###
	vuzfile=os.path.join("userdata", "vuzes.csv")
	print("Saving vuzes...")
	with open(vuzfile, "w", newline='', encoding="utf8") as f:
		wr=csv.writer(f, delimiter=',', quotechar='"')
		for row in vuzes:
			#print(row)
			print("*", end="")
			wr.writerow(row)
		print("")
	print("Done")

	vuzes_tr=[]
	for i in vuzes:
		vuzes_tr.append(i[1])
	tree=wordgroup.gentree(vuzes_tr)
	wordgroup.showtree(tree)
