#!/usr/bin/env python3
import rtfunicode
from os.path import join
default_fs=14
printout_rtf=join("userdata", "printout.rtf")
def printout(vuzes, olymps, marks, version):
	file="{\\rtf\n"
	file +="{\\fs48 {\\b vuz } printout ("+version+") \\fs0}\\par\n{\\upr\\fs"+ format(default_fs*2)+"\n" # there are half-points in rtf
	line="---------"+str(marks)+"----------------------------------"
	file +=line+"\\par\n"
	for i in vuzes:
		i=str(i.encode('rtfunicode'))[1:].replace('\\\\','\\')
		file +="{\\ql "+ i +" \\q0}\\par\n"

	file +="-"*len(line) +"\par\n"
	file +="https://vuzopedia.ru/program/bakispec/<id>\n"

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
