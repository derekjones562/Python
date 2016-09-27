#!/usr/bin/python
import sys
import re
sys.stdout.write(str(len([line for line in sys.stdin.readlines() if re.match(r'\S+', line)]))+'\n');
sys.stdout.flush();
