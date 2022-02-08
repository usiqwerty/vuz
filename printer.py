#!/usr/bin/env python3
import rtfunicode
default_fs=14

def printout(vuzes, olymps, marks, version):
	file="{\\rtf\n"
	file +="{\\fs48 {\\b vuz } printout ("+version+") \\fs0}\\par\n{\\upr\\fs"+ format(default_fs*2)+"\n" # there are half-points in rtf
	line="---------"+str(marks)+"----------------------------------"
	file +=line+"\\par\n"
	for i in vuzes:
		#i=str(bytes(i,'utf-16'))[1:].replace('x','u')
		#i = str(bytes(i,'utf-8'), 'cp1251')
		i=str(i.encode('rtfunicode'))[1:].replace('\\\\','\\')
		file +="{\\ql "+ i +" \\q0}\\par\n"

	file +="-"*len(line) +"\par\n"

	for i in olymps:
		olymp=i.split("http")[0]
		link="http" + i.split("http")[1]
		#olymp=str(bytes(olymp,'utf-16'))[1:].replace('x','u')
		#olymp=str(bytes(olymp, 'utf-8'), 'cp1251')
		olymp=str(olymp.encode('rtfunicode'))[1:].replace('\\\\','\\')
		file +="{\\ql "+ olymp +" \\q0}\\par\n"
		file +="{\\qr "+ link +" \\q0}\\par\n"
	file+="\n}}"
	file=file.replace("'", "")

	f=open('printout.rtf', 'w')
	f.write(file)
	f.close()
