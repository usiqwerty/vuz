#!/usr/bin/env python3
import egevuz,rsr,grades
subjs=['математика','русский язык','физика','общест','история','биология', 'информа', 'химия', 'литература', 'география', 'иностран']
cities={
'Москва':59,
'Санкт-Петербург':50,
'Екатеринбург':83,
'Архангельск':5,
'Астрахань':7,
'Владивосток':76,
'Иваново':23,
'Ростов-на-Дону':68,
'Махачкала':20
}
def main (subj_input, marks, city, ol):
	vuzes, url = egevuz.vuzopedia(marks, city)

	if url=='':
		return ([],[], '')
	#we are using set instead of list
	#to prevent duplicates
	olymps=set()
	if ol:
		for i in subj_input.split(" "):
			school=float(grades.get_average(subjs[int(i)-1]))
			ege=(school-2)*33.3
			if ege>=75:
				for i in rsr.olymps(upd=False, subj=subjs[int(i)-1], lvl=1):
					olymps.add(i)
	return (vuzes, olymps, url)

if __name__=="__main__":
	print("vuz abobus by usiqwerty/2021")

	for i in range(len(subjs)):
		print(i+1, subjs[i])
	subj_input=input("Выберите предметы через пробел: ")

	marks=['']*11
	for i in subj_input.split(" "):
		school=float(grades.get_average(subjs[int(i)-1]))
		ege=(school-2)*33.3
		marks[int(i)-1]=round(ege)

	for i in cities:
		print(cities[i], "\t"+i)
	city=int(input("Введите код города: "))



	ol=input("Олимпиады надо? y/n: ")
	if ol in ["y", "д"] :
		oly=True
	else:
		oly=False
	vuzes, olymps, url = main(subj_input, marks, city, oly)
	if url=='':
		print("Нет подключения к Интернету")
	else:
		print("\nВаши баллы на ЕГЭ предположительно будут такими: ", list(filter(lambda x: x!='', marks)))
		print("На основе этих баллов, вы можете попасть в один из этих вузов:\n")
		for i in vuzes:
			print (i)
		if oly:
			print("\nА так же олимпиады:")
			for i in olymps:
				print (i)
		print("Удачи ;)")
