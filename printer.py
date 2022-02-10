#!/usr/bin/env python3
import rtfunicode
from os.path import join
default_fs=14
printout_rtf=join("userdata", "printout.rtf")
def printout(vuzes, olymps, marks, version, mentioned_vuzes, verbose_vuzes, city):
	file="{\\rtf1\n"
	file +="{\\fs48 {\\b vuz } printout ("+version+") \\fs0}\\par\n{\\upr\n"
	citystr=str(city.encode('rtfunicode'))[1:].replace('\\\\','\\')
	line="---------"+str(marks)+"--------"+citystr+"-----------------"
	file +=line+"\\par\n"
	for i in vuzes:
		i=str(i.encode('rtfunicode'))[1:].replace('\\\\','\\')
		file +="{\\ql "+ i +" \\q0}\\par\n"

	file +="-"*round(len(line)/2) +"\\par\n"
	file +="https://vuzopedia.ru/program/bakispec/<id>\\par\n"
	file +="https://vuzopedia.ru/vuz/<id>\\par\n"

	if verbose_vuzes:
		file +="-"*round(len(line)/2) +"\\par\n"
		for vuz in mentioned_vuzes:
			file+= mentioned_vuzes[vuz] + " " + str(vuz.encode('rtfunicode'))[1:].replace('\\\\','\\') + "\\par\n"
	file +="\\page\n"
	if len(olymps)>1:
		for i in olymps:
			olymp=i.split("http")[0]
			link="http" + i.split("http")[1]
			olymp=str(olymp.encode('rtfunicode'))[1:].replace('\\\\','\\')
			file +="{\\ql "+ olymp +" \\q0}\\par\n"
			file +="{\\qr "+ link +" \\q0}\\par\n"

	file+="\n}}"
	file=file.replace("'", "")
	file=file.replace('"', '')



	f=open(printout_rtf, 'w')
	f.write(file)
	f.close()
