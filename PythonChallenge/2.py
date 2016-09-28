#!/bin/python
#http://www.pythonchallenge.com/pc/def/ocr.html

from source_2 import *
import re

unique=""
for char in page_source:
	if(re.match(r'[A-Za-z]',char)):
		unique+=char

print "http://www.pythonchallenge.com/pc/def/"+unique+".html"
