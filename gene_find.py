
import os
import sys
from Bio import SeqIO


#genome=SeqIO.read('gb_files/Pteridium.gb','genbank')

def make_gene_list(file_name):
    os.chdir('./agb_files')# need to temporarily change to dir with genbank files
    gene_list = []
    for gb_record in SeqIO.parse(open(file_name,"r"), "genbank"):
        print "Name %s, %i features" % (gb_record.name, len(gb_record.features))
        #the above line is just for testing. To see if file is being read.
        for feature in gb_record.features:
            if feature.type == "gene":
                name = str(feature.qualifiers['gene'])
                name = name.strip('[')
                name = name.strip(']')
                name = name.strip("'")

                loc = feature.location.start, feature.location.end
                loc = str(loc)
                loc = loc.replace('ExactPosition','')
                loc = loc.replace('(','')
                loc = loc.replace(')','')
                
                line_list =  [name, loc]
                gene_list.append(line_list)
    os.chdir('..') # Change back to main directory (up one level)
    return gene_list
    

    
#matches = open("cp_match.txt", 'r')
 
# note if loc2 < loc1 (weird genes!)
# no hit - note this and emphasise positoin in genome for manual lookup\
# could easily be rps12, ndhB, or other weirdo.
# Also make sure that you record the position of the entire gene including
# intron!
    
def parse_through_matches(matches):# This is rough
    #May need to open matches file
    cp_list = []
    for line in matches:
        list_line = line.split('\t') 
        if list_line[0] == 'cp:':
            cp_list.write(line)
        elif line[0] == ('\n'): #proably do not need this, but test
            continue
        cp_list.write(line[1])
        cp_list.write('\n')
    #write cp_list to file?
    matches.close()


def make_dictionary_gene_lists(file_list):
    mydict = {}
    for name in file_list:
        mydict[name] = make_gene_list(name)
    return mydict

def list_files(dir):
    file_list = []
    for file_name in os.listdir(dir):
        #print file_name
        file_list.append(file_name)
    return file_list
        
        
if __name__ == "__main__":
    file_list = list_files('./agb_files')
    dictionary_gene_lists = make_dictionary_gene_lists(file_list)
    print dictionary_gene_lists  
    