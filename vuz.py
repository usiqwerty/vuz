#!/usr/bin/env python3
#TODO:printout seems to be very strange and obsolete, maybe it should be deleted
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
	38: "Нанотехнологии и наноматериалы"
}
if __name__=="__main__":

	city=0
	printout=False
	deep=False
	hothead=False
	verbose_vuzes=False
	force=False
	for arg in sys.argv:
		try:
			city=int(arg)
		except:
			if arg=="--update":
				rsr.update()
			elif arg=="--print":
				printout=True
			elif arg=="--deep":
				deep=True
			elif arg=="--verbose":
				verbose_vuzes=True
			elif arg=="--hothead":
				hothead=True
			elif arg=="--force":
				#print("--force option is not implemented")
				force=True
			elif arg=="--help":
				print()
				print(f"{sys.argv[0]} [city_id] [--update] [--print] [--deep] [--verbose] [--force]")
				quit()
			continue
	print ("vuz", version)

	#iterate through subjects and print them
	for i in range(len(subjs)):
		print (str(i+1), "\t"+subjs[i]) #i-th subject
	subjs_input=map( lambda x: int(x)-1 , input("Предметы через пробел: ").split(' ') ) #get int's from string and make index from number
	subs=list(subjs_input) #make list from map object
	###

	#if city's not specified in cmdline
	if city==0 and not hothead:
		for i in cities:
			print(i,"\t"+ cities[i])
		city=int(input("Код города: "))
		print(cities[city]) #choice
	elif hothead:
		city=''
	###
	olmps = True if input("Олимпиады y/n? ")=='y' else False

	#themes
	for i in themes:
		print(i,"\t"+ themes[i])
	theme=int(input("Тематика: "))
	print(themes[theme])
	###
	if printout and not deep and not verbose_vuzes: #deep and verbose modes are restricted to be printed
		verbose_vuzes = True if input("Прописать названия вузов в дополнение к их номерам y/n? ")=="y" else False

	#get marks
	subjects=list(map(lambda x: subjs[x],subs)) #get list of subjects by specified indexes
	grades=grades.get_grades(subjects) #get grades (dict) by suject names

	for subj in grades:
		try:	#translate decimal point and convert to float
			curr=float(grades[subj].replace(',','.'))
			grades[subj]=round((curr-2)*33.3)
		except: #cell could be empty
			continue
	###

	#generate EGE score
	scores=[]
	for subj in subjs: #the sus
		score=''
		if subj in grades:
			if force:
				score=input(f"Балл ЕГЭ по предмету {subj}: ")
			else:
				score=str(grades[subj])
		scores.append(score)
	#scores=['80', '80', '', '', '', '', '80', '', '', '', '']
	#fetch vuzes
	results = egevuz.vuzopedia(scores, city, theme, deep)
	string_results = list(map(' '.join, results)) #make string from each item of 'results' and put into list
	if results[0]==-1:
		print("Нет интернета")
	###
	print("https://vuzopedia.ru/program/bakispec/<id>")
	#olympiads
	if olmps:
		olymps=set()
		for subj in filter(lambda x: int(scores[x])>=75, subs): #get only subjects with enough EGE score
			for i in rsr.olymps(subjs[subj].lower(), 1): #and get olympiads for these subjects
				olymps.add(i)
		for i in olymps:
			print(i)
	else:
		olymps=['Поиск олимпиад не производился']
	###
	if printout:
		print("Generating printout...")
		if not hothead:
			city=cities[city]
		printer.printout(string_results, olymps, list(filter(lambda x: x!='', scores)), version, egevuz.dict_vuzes, verbose_vuzes, city)

	#save results
	vuzfile=os.path.join("userdata", "vuzes.csv")
	print("Saving vuzes...")
	with open(vuzfile, "w", newline='', encoding="utf8") as f:
		wr=csv.writer(f, delimiter=',', quotechar='"')
		for row in results:
			print("*", end="")
			wr.writerow(row)
		print("")
	print("Done")
	###
	result_tr=[]
	for i in results:
		result_tr.append(i[1])
	tree=wordgroup.gentree(result_tr)
	wordgroup.showtree(tree)

