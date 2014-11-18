"""
This script takes genbank fasta files and does some renaming of the headers
so that the returned lines in blast output have the gene names more
readable

Written by Carol A. Rowe
16 Nov 2014
"""
import re
import sys

data = open(sys.argv[1], 'rU')
output = open('temp_out.txt', 'w')
def get_line(inputstring):
    line_re = re.compile("^\\>lcl\\|(\S+).+gene=(\w+).*?(\\[protein=.*?\\])")
    line_search = re.search(line_re, inputstring)
    if line_search:
        return ('>{}_{} [gene={}] {}\n' .format(line_search.group(1), line_search.group(2), line_search.group(2), line_search.group(3)))

for line in data:
    return_line = get_line(line)
    if return_line:
        output.write(return_line)
    else:
        output.write(line)

output.close()
data.close()