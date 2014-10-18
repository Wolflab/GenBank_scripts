fastasplitn

These to C programs take a large fasta file and split into n equal sizes for processing.

The larger version (17 kb) is for Mac and smaller (11.3 kb) is for linux


Fastasplitn: invalid input parameters: n 0 p 0 c 1

Function:  Splits a fasta file into N data streams.
           Default is to send each stream to a separate output file.
           Optional command line parameters are indicated with [].

Usage:     fastasplitn infile N [P [C]]
  infile = input file.  "-" or "stdin" = read from stdin
  N =      number of data streams to produce, N must be >0
  P =      0 or omitted, emit N streams to N files
    =      1->N, only emit contents of Pth stream (1-N), send to stdout
  C =      emit C sequences in order for each stream, C>=1, 1 is default

Examples: in all cases input has 20 sequences

  N=4 P=0 C=5:
    1->5 to file1, 6->10 to file2, 11->15 to file3, 16->20 to file4
  N=4 P=2 C=3:
    4->6,16->17 to stdout

Default fragment file name template is "frag%3.3d"
The string in the symbol SPLITFRAGTEMPLATE overrides this default



