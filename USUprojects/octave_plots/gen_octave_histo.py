#!/usr/bin/python
import re
import sys
outfile = sys.argv[1];
out= open(outfile, 'w')
#print outfile, "\n"
out.write("Y=[\n")
for line in sys.stdin.readlines():
    toop =line.split()
    out.write("\t"+toop[1]+",\n")
    
out.write("];\nfigure;\nbar(Y, 'FaceColor', [0, 0.5, 0.5],\n'EdgeColor', [0, 0.5, 0.5],\n'LineWidth', 2);\ntitle('A440 Note Frequencies');")
out.close()
