#! /usr/bin/env python

import sys

#print sys.path

import pandas as pd
from email_from_gmail import send_email
from email_from_gmail import date_today
from Bio import Entrez

'''This if for searching the NCBI database for new fern chloroplast/plastid genomes of >10,000bp
and then comparing to exisiting file and appending new samples.'''

# The following line finds the path for this script and saves it. Not yet used
# save_path = os.path.dirname(os.path.abspath(__file__))
# can then use like this:
# open(save_path + '/checked_accession_numbers.csv', 'w').close()

#email parameter so the NCBI can contact you if there is a problem
Entrez.email = "paul.wolf@usu.edu" 

#opening and reading the master file
pathway = '/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/Carol_search_files/fern_file.csv'
masterdata = pd.read_csv(pathway, usecols=['id'], dtype=str)

#making sure we have the correct data types
#print masterdata.dtypes

# use entrez SEARCH to search the nucleotide database for the fern (moniliform) chlroplast/pastid sequences greater than 10,000bp.
handle = Entrez.esearch(db="nucleotide", retmax=100, term="Moniliformopses[orgn] AND (plastid[titl] OR chloroplast[titl]) AND 10000:999999[slen]")
data = Entrez.read(handle)
#return the id list of matches
dataL = data['IdList']
handle.close()
#just checking to see how many hits and printing the id list too
body1 = "The new search generated {0} hits" .format(data['Count'])
body2 = "The master data has {0} hits". format(len(masterdata))


#now convert the masterdata id column to a list so that we can compare lists:
masterid = masterdata['id'].tolist()
#print masterid

#New items in new list (dataL) that is not in the master list
newsamples = list(set(dataL) - set(masterid))

#Here are samples that are in the master list, but not the new list!
confusedsamples = list(set(masterid) - set(dataL))
message  = ""

if len(masterid) > len(dataL):
    body3 = body1 + "\n" + body2 + "\n" + "You better contact your wife! Something's wrong; new search results shorter than master list. Chocolate may help the situation."
    send_email("paul.wolf@usu.edu", date_today() + " - GenBank search for Fern plastid Genomes", body3)
elif len(masterid) == len(dataL):
    empty = []
    if newsamples == empty:
        body4 = body1 + "\n" + body2 + "\n" + 'Nothing new. Lists are the same length and all items match. Maybe you should get into the lab and generate some data.'
        send_email("paul.wolf@usu.edu", date_today() + " - GenBank search for Fern plastid Genomes", body4)
        message = body4
    else:
        body5 = "The new search has the following, which is not in the master list."
        body6 = str((newsamples))
        body7 = "The master list has the following, which is not in the new list."
        body8 = str((confusedsamples))
        body9 =  body1 + "\n" + body2 + "\n" + body5 + "\n" + body6 + "\n" + body7 + "\n" + body8
        send_email("paul.wolf@usu.edu", date_today() + " - GenBank search for Fern plastid Genomes", body9) 
        message = body9
else:
    outlist = []
    for item in newsamples:
        #Use entrez fetch to search NCBI nucleotide database for each new sample (item). Returns an xml file that will get parsed
        Fasthandle = Entrez.efetch(db="nucleotide", id=item, retmode="xml")
        recorded = Entrez.read(Fasthandle)
        Fasthandle.close()
        #This returns the id number and the source info
        outlist.append([item, recorded[0]["GBSeq_source"]]) 
    #write your output to a dataframe (csv file). Fill in your own pathway!
    my_df = pd.DataFrame(outlist, columns=['id', 'source'])
    body10 =  "Here is the list of new samples:"
    body11 = str(outlist)
    body12 = body10 + "\n" + body11
    send_email("paul.wolf@usu.edu", date_today() + " - GenBank search for Fern plastid Genomes", body12)
    message = body12
    #Opening and reading master file with both columns for appending new data
    Appendmasterdata = pd.read_csv(pathway, dtype=str)
    #Now appending the new data (my_df) to the master file (Appendmasterdata)
    NEWmasterdata = Appendmasterdata.append(my_df, ignore_index=True)
    #Convert to csv and save.
    NEWmasterdata.to_csv(pathway, index=None)

log = open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/Carol_search_files/cp_search_log.txt', 'a')
log.write(date_today() + ", " + message + '\n')