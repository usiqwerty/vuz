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
