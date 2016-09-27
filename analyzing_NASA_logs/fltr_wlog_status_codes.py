#!/usr/bin/python
import sys
import re
code = sys.argv[1];
for line in sys.stdin.readlines():
    splitLog = line.split()
    if(splitLog[8]== code):
        sys.stdout.write(line)
sys.stdout.flush()
