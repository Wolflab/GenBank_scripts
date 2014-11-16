#!/usr/bin/perl
# This from Josh Der Cal State Fullerton
open OUT, ">tmp";
while(<>){ 
	if (/^>lcl\|(\S+).+gene=(\w+).*?(\[protein=.*?\])/){ 
		print OUT ">$1_$2 [gene=$2] $3\n"; 
	}	
	else{print OUT $_;} 
}
