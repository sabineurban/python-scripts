#!/usr/bin/env python
# python 2.7
# Sabine Urban, 2019-01-29

# Import libraries
from Bio import SeqIO
import sys
import argparse

# Parse the command line arguments.
parser=argparse.ArgumentParser(description="Sort and subset fasta files based on a textfile.")
parser.add_argument('-t', '--textfile', dest="textfile", required=True, help='A text \
file with individuals to include and the order they should be sorted in. One individual per line as given in the fasta file, e.g. >species_A')
parser.add_argument('-i', '--infile', dest="infile", required=True, help='The input fasta file name.')
parser.add_argument('-o', '--outfile', dest="outfile", default=sys.stdout, help='The output file name. If not specified will print to stdout.')
args=parser.parse_args()
textfile = args.textfile
infile = args.infile
outfile = args.outfile

# start an empty list for the IDs
ID_list = []

# make a list of the IDs
with open(textfile, "r") as handle:
	for record in SeqIO.parse(handle, "fasta"):
    # add each record ID to the list
		ID_list.append(record.id)

print(ID_list)

# iterate over the IDs, save the matching fasta entries
for my_ID in ID_list:
    # print my_ID
    for record in SeqIO.parse(open(infile, "r"), "fasta"):
        if my_ID in record.id:
            # for appending to the output file
            output_handle = open(outfile, "a")
            SeqIO.write(record, output_handle, "fasta")
            print("writing:")
            print(my_ID)
            output_handle.close()
            
print("done")