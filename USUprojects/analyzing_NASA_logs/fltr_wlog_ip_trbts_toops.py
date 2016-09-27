#!/usr/bin/python
import sys
import re
transfered_bytes="";
for line in sys.stdin.readlines():
    twotoop=[]
    splitLog = line.split()
    ip = splitLog[0]
    for temp in splitLog:
        if (re.match(r'^\d',temp)):
            transfered_bytes=temp
    twotoop.append(ip)
    twotoop.append(transfered_bytes)
    sys.stdout.write(str(twotoop[0])+" " +str(twotoop[1])+"\n")
sys.stdout.flush()
