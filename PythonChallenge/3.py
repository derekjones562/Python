#!/bin/python
#http://www.pythonchallenge.com/pc/def/equality.html

import re
from source_3 import *

small_with_bodyguards=""
pattern="[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

small_with_bodyguards=re.findall(pattern, page_source)

small_people_unite=""
for letter in small_with_bodyguards:
	small_people_unite+=letter
print "http://www.pythonchallenge.com/pc/def/%s.html" % (small_people_unite)
