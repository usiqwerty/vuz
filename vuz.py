#!/usr/bin/env python3
import egevuz,rsr,sgo

print("vuz abobus by usiqwerty/2021")
subjs=['математика','русский язык','физика','общест','история','биология', 'информа', 'химия', 'литература', 'география', 'иностран']
for i in range(len(subjs)):
	print(i+1, subjs[i])
marks=['']*11
choice=input("Выберите предметы через пробел: ")
ol=input("Олимпиады надо? y/n: ")
#d={'mat':'','rus':'','fiz':'','obshe':'','ist':'','biol':'','inform':'','him':'','liter':'','georg':'','inyaz':''}
#print(d)

for i in choice.split(" "):
	print(int(i)-1, subjs[int(i)-1])
	school=float(sgo.get_average(subjs[int(i)-1]))
	ege=(school-2)*33.3
	marks[int(i)-1]=round(ege)
print("\nВаши баллы на ЕГЭ предположительно будут такими: ", list(filter(lambda x: x!='', marks)))
print("На основе этих баллов, вы можете попасть в один из этих вузов:\n")
egevuz.vuzopedia(marks, 83)

olymps=set()
if ol=="y":
	oly=True
	print("\nА так же олимпиады:")
	for i in choice.split(" "):
		school=float(sgo.get_average(subjs[int(i)-1]))
		ege=(school-2)*33.3
		if ege>=75:
			for i in rsr.walkthrough(upd=False, subj=subjs[int(i)-1], lvl=1):
				olymps.add(i)
for i in olymps:
	print(i)
print("Удачи ;)")