"""26 April, 2014  Code written by Paul Wolf

This script takes three blast output files from contigs that have matches to
nuclear (nc), chloroplast (cp) and mitochondrial (mt) gene and genome databases.
The script loops through the nuclear contig matches and then looks to see if 
that same contig is in either the cp, mt, or both. Any matches are written to 
a file. Note that this script does not find matches between cp and mt only (with
no matchh to nc). The separate script cp_mt_blast_out_compare.py does that. 
So far the few matches between cp and and mt, are also in nc.


"""
#open files
nc_data = open("Cystopteris_clc_k31.aablast.out", 'r')
cp_data = open("Cystopteris_clc_k31.cp_blast.out", 'r')
mt_data = open("Cystopteris_clc_k31.mt_blast.out", 'r')
nc_cp_mt_compare = open("22nc_cp_mt_compare.txt", 'w')

#put cp and mt into lists
cp_list = []
for line in cp_data:
    cp_list.append(line)
    
mt_list = []
for line in mt_data:
    mt_list.append(line)

cp_count = 0
mt_count = 0
for nc_line in nc_data:
    cp_match = False
    nc_newline = nc_line.split('\t')
    for cp_line in cp_list:
        cp_newline = cp_line.split('\t')
        if cp_newline[0] == nc_newline[0]:
            cp_match = True 
            cp_linetxt = "cp:\t" + cp_line
            nc_linetxt = "nc:\t" + nc_line
            nc_cp_mt_compare.write('\n')
            nc_cp_mt_compare.write(nc_linetxt)
            nc_cp_mt_compare.write(cp_linetxt)
            cp_count+=1
    for mt_line in mt_list:
        mt_newline = mt_line.split('\t')
        if mt_newline[0] == nc_newline[0]:
            mt_linetxt = "mt:\t" + mt_line
            if cp_match == False:
                nc_cp_mt_compare.write('\n')
                nc_linetxt = "nc:\t" + nc_line
                nc_cp_mt_compare.write(nc_linetxt)
            nc_cp_mt_compare.write(mt_linetxt)
            mt_count+=1           
print "cp matches: ", cp_count
print "mt matches: ", mt_count

cp_data.close()
mt_data.close()
nc_data.close()
nc_cp_mt_compare.close()