"""
Start with a blast table from the CLC assembly as query and cp genomes as db
(CLC_to_cp_genomes). To this you want to compare the table from  blast of the
plastome (1 x IR) as query and CLC assembly (remove Ns) as db
(plastome_to_CLC). Lots of overlap between the two. Also need list of true cp
contigs. This script will take the CLC_to_cp_genomes and let you know which
lines are real cp (removes them) which are in the plastome_to_CLC (removes them
too). What you are left with is a set of unique lines that you then add to the 
CLC_to_cp_genomes to get a complete list.

NOte that at some point you need to determine which hits are unique. In the
CLC_to_cp_genomes blast the same part of a query may have hit different
genomes. These can be removed by a modification of
calc_total_mt_seq_in_assembly.py


"""


real_cp_list = ['contig_79','contig_18','contig_106','contig_260823','contig_266','contig_894362','contig_704449','contig_234178','contig_153895','contig_298687']

plus_file = open('Ceratopteris_temp_plus.csv', 'r')
plus_list  = []
for line in plus_file:
    temp2_line = line.split(',')
    temp2_line[1]
    plus_list.append(temp2_line[1])
    
print 'plus_list = ', plus_list, 'end plus'
new_file = open('new_file.csv', 'w')

clc_to_cp = open ('temp_cerat.csv', 'r')
clc_to_cp_contig_list = []
for line in clc_to_cp:
    temp_line = line.split(',')
    if temp_line[0] in real_cp_list:
        print temp_line[0], ' in real cp list'
    elif temp_line[0] in plus_list:
        print temp_line[0], ' in plus list'
    else:
        new_file.write(line)


    
plus_file.close()    
new_file.close()
clc_to_cp.close()