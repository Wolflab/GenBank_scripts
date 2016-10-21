import pandas as pd
from Bio import Entrez

#todo: 
# 1. Change file paths and email address. 
# 2. Note if there is a new one by comparing to old list (dataframe)
# 3. Email self if new record, or no new records.
# 4. Automate for once a month

#email parameter so the NCBI can contact you if there is a problem
Entrez.email = "paul.wolf@usu.edu" 
# use entrez SEARCH to search the nucleotide database for the fern (moniliform) chlroplast/pastid sequences greater than 10,000bp.
handle = Entrez.esearch(db="nucleotide", retmax=100, term="Moniliformopses[orgn] AND (plastid[titl] OR chloroplast[titl]) AND 10000:999999[slen]")
data = Entrez.read(handle)
#return the id list of matches
dataL = data['IdList']
handle.close()
#just checking to see how many hits and printing the id list too
#print data['Count']


'''
#just playing here. Another way to get info. You could pass a list to get all in dataL.
newhandle = Entrez.esummary(db="nucleotide", id="966201822")
record = Entrez.read(newhandle)
print record[0]["Id"]
print record[0]["Title"]
newhandle.close()
'''           
#Now use entrez FETCH to retrieve the 'source' info. Can also get other fields such as sequence, definition, etc. here if you wanted to
#putting the output into a list of lists for easy writing to a dataframe - see next section
outlist = []
for item in dataL:
    Fasthandle = Entrez.efetch(db="nucleotide", id=item, retmode="xml")
    recorded = Entrez.read(Fasthandle)
    Fasthandle.close()
    outlist.append([item, recorded[0]["GBSeq_source"]]) 

#write your output to a dataframe (csv file). Fill in your own pathway!
my_df = pd.DataFrame(outlist)
my_df.columns = ["id", "source"]
pathway = '/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/Carol_search_files/fern_file.csv'
my_df.to_csv(pathway, index=False)

print "all done"
