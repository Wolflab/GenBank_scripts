#!/usr/bin/env python

# Takes a single FASTQ file and splits to .fasta + .qual files
# usage: python fastq_to_fasta.py inputfilename.fastq
# script taken from http://nebc.nerc.ac.uk/tools/code-corner/
# scripts/sequence-formatting-and-other-text-manipulation#-ace2fastacontigs-pl
# Author:
# Tim Booth, based on script fragment found in BioPython docs:
# http://www.biopython.org/DIST/docs/api/Bio.SeqIO.QualityIO-module.html#PairedFastaQualIterator


import sys
from Bio import SeqIO

if len(sys.argv) == 1: 
	print "Please specify a  single .fastq file to convert."
	sys.exit()

filetoload = sys.argv[1]
basename = filetoload

#Chop the extension to get names for output files
if basename.find(".") != -1:
	basename = '.'.join(basename.split(".")[:-1])

SeqIO.convert(filetoload, "fastq", basename + ".fasta", "fasta")
SeqIO.convert(filetoload, "fastq", basename + ".qual", "qual")