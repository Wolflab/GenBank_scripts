#! /usr/bin/env python

"""
add_contig_proportion.py
Paul G. Wolf
25 May, 2014

IMPORTANT INSTRUCTIONS FOR RUNNING SCRIPT:

Arguments needed in this order:
script name (add_contig_proportion.py)
name of multi fasta file (including path)
name of blast output table
column in which the contigs appear in your blast table (should be '0' for first
column or '1' for second column, etc). ** see more details below:

This script takes a multifasta file and a resulting blast output(-outfmt 6). The
fasta file could have been either the query or the database. For each hit in 
table the script will look at the length of contig aligned and divide that by the
length of the contig. The output will be a new file with the same name plus the
word "plus" appended. The contig proportions will be in far right column.

Because this script works for the multifasta file as both query and db, you need
to tell it which one. The only important thing is to open the table you want to 
modify and look to see which column has the contigs that correspond to those in
the multi fasta file. They should should be first or second (0 or 1) columns.
You could get it to work for other table formats only by editing the script.

This provides yet another measure of how good the blast hit
is. If there are many such hits to a large contig then low proportions would be
expected. But if the contig has one or a few hits then a low proportion suggests
that the hit may be bogus. This is appropriate for such situations as blasting
a shotgun assembly to a mitochondrial or chloroplast genome db, or blasting an
organellar genome to a shotgun assembly.

"""

import sys
from Bio import SeqIO


def add_contig_proportions(blast_output_table,contig_len_dict, column):
    data = open(blast_output_table, 'r')
    new_table = open(blast_output_table + "_plus", 'w')
    if column == '0':
        start = 6; end = 7 #note: if your table has the contig hit positions
    else:#          elsewhere, then replace int(start) and int(end) accordingly
        start = 8; end = 9
    for line in data:
        linelist = line.split('\t')
        hit_len = abs(int(linelist[int(start)]) - int(linelist[int(end)]))
        prop = float(hit_len)/contig_len_dict[linelist[int(column)]]
        if (hit_len) > contig_len_dict[linelist[int(column)]]:
            print "You have blast hits longer than contig. Probably using wrong columns"
        prop = "{0:.3f}".format(prop)
        line = line.strip('\n')
        newline = line + '\t' + prop + '\n'
        new_table.write(newline)
    new_table.close()
    data.close()
 
def contig_lengths(fasta_file):
    #create our hash table (dictionary) of contigs and their lengths
    lengths={}
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        lengths[seq_record.id]= len(seq_record.seq)
    #print len(lengths)
    return lengths

 

def main():
    userParameters=sys.argv[1:]
    if len(userParameters) != 3:
        print "wrong number of arguments entered"
    else:
        if (sys.argv[3] == '0') or (sys.argv[3]) == '1':
            print "Program is running"
            print "Drink coffee or go for a run!"
            fasta_file = sys.argv[1]
            blast_output_table = sys.argv[2]
            column = sys.argv[3]
            contig_len_dict = contig_lengths(fasta_file)
            add_contig_proportions(blast_output_table,contig_len_dict, column)
        else:
            print 'you must type "0" or "1" for final argument, or edit script'
    
if __name__ == "__main__":
    main()