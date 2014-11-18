#!/usr/bin/env python

'''
Splits a single file of multiple contigs into a directory of multiple files.
The split is based upon: > 
Each new file is a single contig. 
File name includes contig name.
Usage: contig_splitter.py  filename  new_prefix

Author:
Carol A. Rowe 2014-11-17 carol.rowe666@gmail.com
'''

import re
import os
import sys

data = open(sys.argv[1], 'rU')

# User needs to enter 3 fields listed in print statement for program to run.
if len(sys.argv) != 3:
    print "Usage: contig_splitter.py  filename  new_prefix"
    sys.exit()

# Search for pattern within the large file to get the new name for the new,small file
def get_file_name(inputfile):
    new_file_re = re.compile('\\>.+')
    new_file_name = re.search(new_file_re, inputfile)
    if new_file_name:
        return new_file_name
    
# Creating the name of the new directory in which to put the new files.    
# Checks to see if direcotry already exists. If it does, it uses that.
name = sys.argv[1].split('.')
dir_name = name[0]    
try:
    os.makedirs(dir_name)
except OSError:
    # If folder already exists, us it.
    pass

# Summarizing the pathway name to put files into
pathway = os.path.join(dir_name, sys.argv[2])

# Executing the program to create new contig files and putting them into the new folder.
for line in data:
    new_file = get_file_name(line)
    if new_file:
        name = line.strip('>')
        name = name.rstrip()
        output = open(pathway + name + '.fasta', 'w')
        output.write(line)
    else:
        output.write(line)
        output.close()

data.close()
