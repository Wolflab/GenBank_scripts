#! /usr/bin/env python
from __future__ import print_function
import re
import sys

"""This script will take a sequin .tbl file that you just spent ages correcting
only to find that you need to add a bunch of nucleotide positions to the entire
genome. Set up for chloroplast genomes. Also set up to add numbers to ALL 
positions. Would need adjusting so that the new bases are added (or removed)
starting at a specified position.

Use:

./adjust_numb.py <filename> number of bases to add

Prints to stdout, so redirect to new file if needed

"""
def adjust(table, numb):
    #adjusted = open("adjusted.tbl", 'w')
    for line in table:
        line.strip('\r')
        newline = ""
        if "pos" in line:# deal with things like RNA editing annotations
            line_start = "\t\t\ttransl_except\t(pos:complement("
            searchstr = '(\(pos:complement\()(\d+)\.\.(\d+)(.+)'
            result = re.search(searchstr,line)
            new_first = int(result.group(2)) + int(numb)
            new_sec = int(result.group(3)) + int(numb)
            newline = line_start + str(new_first) + ".." + str(new_sec) + result.group(4)
            print(newline)
        elif line[0].isdigit():# lines with regular feature positions
            line = line.split('\t')
            newnumb1 = str(int(line[0]) + int(numb))
            newnumb2 = str(int(line[1]) + int(numb))
            if len(line) > 2:# lines with CDS etc
                newline = newnumb1 + '\t' + newnumb2 + '\t' + line[2]
            else:
                newline = newnumb1 + '\t' + newnumb2 + '\n'
            print(newline, end = '')
        else:
            print(line, end = '') 



def main():
    table_file = sys.argv[1]
    numb = sys.argv[2]
    table = open(table_file, 'r')
    adjust(table, numb)
    #for line in table:
    #    print line
    table.close()

    
if __name__ == "__main__":
    main()