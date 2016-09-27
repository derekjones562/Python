#!/usr/bin/python
import re
import sys

for line in sys.stdin.readlines():
    for temp in line:
        if(re.match(r'-', temp)or re.match(r'_',temp)):
            sys.stdout.write("\t")
        else:
            sys.stdout.write(temp)
