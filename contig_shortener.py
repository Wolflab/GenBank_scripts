#! /usr/bin/env python

"""
This script will take a fasta file (or multifasta file) and use it to create
a new file called short_seq.txt. In this new file, long contigs are split into
smaller contigs of length specified by user

Usage:

./contig_shortener <input_file_name> <max_length_of_contigs>

Beware of funcky stuff:
If your contig is, say, 101 bp long and you shorten to max length of 10, then the
last contig will only have one bp. That is probably fine for most situations, just 
be aware.  Fixing this would require some precalculations to determine how best 
to split the contig.


"""
import sys


def make_short_contigs(input_file,max_seq_length):
    data = open(input_file, 'rU')
    newfile = open('short_seq.txt', 'w')
    for line in data:
        if line[0] == '>':
            header = line.strip()
        else:
            count = 1# This is just to have a number on the new headers
            line = line.strip('\n')# so you don't have unwanted empty lines in output
            for i in xrange(0,len(line),max_seq_length):#this loops through in steps
                new_header = header + "_" + str(count) + '\n'
                new_seq = line[i:i+max_seq_length] + '\n' # This is cutting out the new chunk
                newfile.write(new_header)
                newfile.write(new_seq)
                count+=1
    data.close()
    newfile.close()

if __name__ == "__main__":
    input_file = sys.argv[1]
    max_seq_length = int(sys.argv[2])
    make_short_contigs(input_file,max_seq_length)
