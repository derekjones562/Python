#!/usr/bin/python
import sys
import re
listoftoops=[]
outtoops=[]
for line in sys.stdin.readlines():
    #print line+"\n"
    compare = line.split()
    #print compare[1]
    #print compare
    position =0
    for i in listoftoops:
        toop = i.split()
        #print "toop[1]>compare[1]:"
        #print toop[1]+" > "+compare[1]
        if(int(toop[0]) < int(compare[0])):
            #print "++\n"
            position+=1
        else:
            break
        #splice (listoftoops,position,0, line)
    
    
    listoftoops.insert(position,line)
#print listoftoops
for toop in listoftoops:
    #print toop
    sys.stdout.write(toop)
#sys.stdout.write(str(listoftoops))
sys.stdout.flush();
