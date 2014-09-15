#! /usr/bin/env python
import sys
from Bio import SeqIO

#modified by Paul Wolf 23 May, 2014
"""
This script takes a [list] of contigs that need to be removed from an assembly, 
and an assembly file. Appropriate contigs are then removed.
This is used to to sequenctially remove plastid then mitochondrial assemblies
to leave supposedly nuclear-only assemblies.

Note: You can change name of output file (might add that as argument later)

Either put this function into find_mt_contigs_all_blasts.py or copy out from
find_mt_contigs_all_blasts.py (unique_contig_list) and paste in as 
contigs_to_strip_list here.
"""
 
def contig_stripper(fasta_file,contigs_to_strip_list):
    #create our hash table (dictionary) to add the sequences
    sequences={}
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        #Take the current sequence
        sequence=str(seq_record.seq).upper()
        if seq_record.id in contigs_to_strip_list:
            print seq_record.id
        else:
            sequences[sequence]=seq_record.id
    #Write the clean sequences
    #Create a file in the same directory where you ran this script
    output_file=open(fasta_file + "_minus_cp","w+")
    for sequence in sequences:
        output_file.write(">"+sequences[sequence]+"\n"+sequence+"\n")
    output_file.close()
    print "Contigs removed\nPlease check new file"

 
def strip_arrow(contig_list):#just in case you are dumb enough to include the >
    newlist = []
    for i in contig_list:
        clean_contig = i.strip('>')
        newlist.append(clean_contig)
    return newlist

def main():
    assembly=sys.argv[1]
    print "Program is running"
    print "Drink coffee or go for a run!"
    contigs_to_strip_list = ['contig_3', 'contig_5', 'contig_14']
    contig_stripper(assembly,contigs_to_strip_list)
    
    
if __name__ == "__main__":
    main()