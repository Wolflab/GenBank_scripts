#! /usr/bin/env python
import sys # importing the sys module

# line 1 tells the computer that this is a python file

# Script to correct .gb files for submitting plastome annotation and sequence
# to GenBank using Geneious (version?)
# This script is written in Python 2.7
# May 20 2017
# Paul G Wolf (paul.wolf11@gmail.com) with help from Tanner Robison and Carol A Rowe (as usual)

# Let's start by reading in Tanner's file with gene names and product names
# Read in lines and enter into a Python dictionary
# A dictionary (hash table in other languagfes) is a series of "keys" (labels in this case)
# Each key has its own value. You can then use the key to return the value.
# Much more memory efficient than a list. No need to loop


# first read in file (don't forget to close it later!)
# First I removed double spaces, then removed last few empty lines!

with open('PlastomeCDSproducts.txt', 'rU') as product_names:
    product_dictionary = {line.split(': ')[0]:line.strip("\n").split(': ')[1] for line in product_names}

# Now open the .gb file

gb = open("Azolla_mexicana_139_cp_v0.4.gb", 'rU') # Manually change file name as needed!

# I will use a simple print statement. Then when you run this from command line you can pipe to file
# I will read a line and print it immediately
# if I see the label text I will add the approriate line
# first lets make a switch to see if we should add a product line. This must not be done after
# a line containing the text "  gene  ", but added after "CDS" etc. Start by setting the switch to false.

log_text = "" # just to keep track of weird stuff
cds = False
for line in gb:
    line = line.strip("\n") # strip the carriage return to prevent extra empty lines
    if "  CDS  " in line:
        cds = True
    if "  tRNA  " in line:
        cds = True
    if "  rRNA  " in line:
        cds = True
    if "  gene  "in line:
        cds = False
    if cds == True and "/label" in line: # while not just following a "gene"
        name = line.split("=")[1].strip('"').split(" CDS")[0] # pull out just the gene name to look up product     
        if name in product_dictionary.keys():
            prod = product_dictionary[name]
        else:
            prod = name # if gene not in the list then give it a dummy name and add to log_text
            log_text += prod + "\n"
        print line # just print the line as is for the new file
        # Now add the product line, but strip away extra carriage return for some dumb reason
        new_line = '                     /product="' + prod +'"'
        new_line = new_line.strip("\n")
        print new_line
    else:
        print line # just print the line as is for the new file
gb.close()

#print log_text
print product_dictionary

