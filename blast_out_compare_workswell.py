

nc_data = open("Cystopteris_clc_k31.aablast.out", 'r')
cp_data = open("Cystopteris_clc_k31.cp_blast.out", 'r').readlines()
mt_data = open("Cystopteris_clc_k31.mt_blast.out", 'r').readlines()
nc_cp_mt_compare = open("nc_cp_mt_compare.txt", 'w')

count = 0
for nc_line in nc_data:
    cp_match = False
    nc_newline = nc_line.split('\t')
    for cp_line in cp_data:
        cp_newline = cp_line.split('\t')
        if cp_newline[0] == nc_newline[0]:
            cp_match = True 
            cp_linetxt = "cp:\t" + cp_line
            nc_linetxt = "nc:\t" + nc_line
            nc_cp_mt_compare.write('\n')
            nc_cp_mt_compare.write(nc_linetxt)
            nc_cp_mt_compare.write(cp_linetxt)
            count+=1
    for mt_line in mt_data:
        mt_newline = mt_line.split('\t')
        if mt_newline[0] == nc_newline[0]:
            mt_linetxt = "mt:\t" + mt_line
            if cp_match == False:
                nc_cp_mt_compare.write('\n')
                nc_linetxt = "nc:\t" + nc_line
                nc_cp_mt_compare.write(nc_linetxt)
            nc_cp_mt_compare.write(mt_linetxt)
            count+=1           
print count


nc_data.close()
#cp_data.close()
nc_cp_mt_compare.close()