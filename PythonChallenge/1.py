#!/bin/python
#http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans

scrambled_phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet="abcdefghijklmnopqrstuvwxyz"
key=""
for letter in alphabet:
	key+=chr((ord(letter)-17)%26+97)
table = maketrans(alphabet, key)

print scrambled_phrase.translate(table)+"\n"

print "URL= http://www.pythonchallenge.com/pc/def/"+"map".translate(table)+".html"
