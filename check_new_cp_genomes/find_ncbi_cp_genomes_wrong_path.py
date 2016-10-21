import urllib2
import re
import os.path

keyword = 'Moniliformopses'
#url that has all the accession numbers on the html page
url = 'http://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=2759&opt=plastid'

#Request object used to set things up
req = urllib2.Request(url=url)
#execute request
f = urllib2.urlopen(req)
#save to content as a string
content = f.read()
f.close()

oldList = []
if(os.path.exists(os.getcwd()+'checked_accession_numbers.csv')):
    oldListFile = open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomeschecked_accession_numbers.csv');
    for line in oldListFile:
        oldList.append(line.strip())
    oldListFile.close();
else:
    open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/checked_accession_numbers.csv', 'w').close()

if not os.path.exists(os.getcwd()+'accession_numbers.csv'):
    open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomesaccession_numbers.csv', 'w').close()


#the regular expression used to find the accession numbers
matches = re.findall('<td><a (.*)>(\w{2}_?\d*)<\/a><\/td>', content)


#Saves accession numbers to output.csv
print 'Found',len(matches),'accession numbers.'
x = 0;
for match in matches:
    print 'Checking if ' + str(x)+' matches keyword.'
    if match[1] not in oldList:
        #used to collect the id from accession number
        acc_base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term='+match[1]+'[Accession%20ID]'
        uidContent = urllib2.urlopen(urllib2.Request(url=acc_base)).read()
        #Matches anything that looks like this:
        #<Id>(any number of numbers)</Id>
        idMatch = re.search('<Id>(\d*)<\/Id>', uidContent)
        if idMatch:
            uid = idMatch.group(1)
            fetch_base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id='+uid
            docContent = urllib2.urlopen(urllib2.Request(url=fetch_base)).read()
            if docContent.find(keyword) > -1:
                outputFile = open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/accession_numbers.csv', 'a')
                outputFile.write(match[1]+'\n')
                outputFile.close()
        else:
            if(os.path.exists(os.getcwd()+'/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/checked_accession_numbers.csv')):
                manualCheckFile = open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/manual_check.csv', 'a')
                manualCheckFile.write(match[1]+'\n')
                manualCheckFile.close()
            else:
                manualCheckFile = open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/manual_check.csv', 'w')
                manualCheckFile.write(match[1]+'\n')
                manualCheckFile.close()
        #fetch the article thing and search for keyword
        oldListFile = open('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/checked_accession_numbers.csv', 'a')
        oldListFile.write(match[1]+'\n')
        oldListFile.close()
    else:
        print str(x)+' already checked.'
    x+=1
