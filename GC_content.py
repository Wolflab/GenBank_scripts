
# function to determine GC content of string
def GC(seq):
    c = seq.count("C"); g = seq.count("G")
    return 100*(g+c)/float(len(seq)