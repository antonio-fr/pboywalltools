#!/usr/bin/env python
# coding=utf8


import sys, os, pickle
#from CryptoPlatinum import *

with open('bitcoin/french.txt',mode="rb") as file:
	wordlistdata = file.read()
wordlist_french = wordlistdata.split('\n')

def fl6(w):
	if len(w.decode("ascii","ignore"))==6:
		return True
	else:
		return False

wl = wordlist_french
wlf = filter(fl6, wl)
print len(wl)
print len(wlf)
print wlf
print u"caméra".encode("utf8") in wlf
with open('list6l',mode="wb") as fileout:
	pickle.dump(wlf, fileout)

