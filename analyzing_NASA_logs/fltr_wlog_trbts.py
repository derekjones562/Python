#!/usr/bin/python
import sys
import re
transfered_bytes = ""
for line in sys.stdin.readlines():
    for temp in (line.split(r' ')):
        #print temp
        #print re.match(r'^\d',temp)
        if (re.match(r'^\d',temp)):
            #print "startsk with digit:"
            transfered_bytes = temp
    sys.stdout.write(transfered_bytes)
sys.stdout.flush();

