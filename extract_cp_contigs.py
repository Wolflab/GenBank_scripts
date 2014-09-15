"""This set of functions is for looking at a subset of contigs in an assembly.
In this case, those contigs that are cp or mt. You can  report the 
length of those contigs and also extract them to a separate multi fasta file

"""

from Bio import SeqIO


def extract_cp_contigs(handle,cp_list):
    out = open('Cystopteris_cp_contigs.fasta', 'w')
    for record in SeqIO.parse(handle, "fasta") :
        if record.id in cp_list:
            newline = str(record.id) + '\n' + str(record.seq) + ('\n')
            out.write(newline)
    out.close()
            
def print_lengths_cp_contigs(handle,cp_list):
    for record in SeqIO.parse(handle, "fasta") :
        if record.id in cp_list:
            print record.id, len(record.seq)
            
if __name__ == "__main__":
    handle = open("Cystopteris_clc_k31.fasta", "rU")
    cp_list = ('contig_14', 'contig_45', 'contig_354', 'contig_763', 'contig_1348', 'contig_1459')
    extract_cp_contigs(handle,cp_list)
    #print_lengths_cp_contigs(handle,cp_list)
    handle.close()
