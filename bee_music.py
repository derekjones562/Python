#!/usr/bin/python

############################################################
## bee_music.py
############################################################

from os import listdir
from os.path import isfile, join
import sys
import re

def merge_files_for_pat(drcty, pat):#, merged_fp):
    dirfiles = filter(lambda x: re.match(pat, x) != None, [f for f in listdir(drcty) if isfile(join(drcty, f)) ])
    return dirfiles
    

def gen_no_play_file(filepath):
    #print filepath
    noplayfile= filepath.split (r'.')
    with open(filepath, 'r') as IN:
        with open(noplayfile[0]+"_no_play.txt", 'w') as NOPLAYOUT:
            #print OUT "test"
            IN.readline()
            for noteline in IN:
                #print noteline+"\n"
                if not re.search(r'^\s', noteline):
                    index=2
                    s = noteline.split(r'[')
                    #print s[index]+"\n"
                    if re.search(r'\w',s[1]):
                        index=1
                    notes=s[index].split(r']')
                    NOPLAYOUT.write( notes[0]+"\n")
            NOPLAYOUT.close()
        IN.close()

def merge_bee_music_files_for_freq(freq, bee_music_dir, bee_music_merged_file):
    if ( freq == 44100 or freq == 22050 or freq == 11025 or freq == 5512 ):
        datePat="\\d{4}-\\d{2}-\\d{2}"
        timePat="\\d\\d-\\d\\d-\\d\\d"
        line_pat = datePat+"\_"+timePat+"\_"+str(freq)+"\_logo\.txt"
        files =merge_files_for_pat(bee_music_dir,line_pat)
        with open(bee_music_merged_file, 'w') as OUT:
            flag=1
            for i in files:
                gen_no_play_file(bee_music_dir+i)
                with open(bee_music_dir+i,'r')as IN:
                    noteline = IN.readline()
                   #print ""+noteline+"\n"
                    if(flag!=0):
                        OUT.write(noteline)
                        flag=0
                    for noteline in IN:
                       if not re.search(r'^\s',noteline):
                          OUT.write(noteline)
                    IN.close()
            OUT.close()
    else:
        print 'Unknown frequency ' + str(freq)
    

## get command line args and go
if __name__ == '__main__':
    #merge_bee_music_files_for_freq(44100,"py_test_data/", "py_test_data/merged_44100.txt")
    merge_bee_music_files_for_freq(int(sys.argv[1]), sys.argv[2], sys.argv[3])
    
        
