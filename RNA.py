#!/usr/bin/env python
'''
Rosalind #: 002
Rosalind ID: RNA
Problem Title: Transcribing DNA into RNA
URL: http://rosalind.info/problems/rna/
'''

def DNA_to_RNA(seq):
    '''
    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    '''
    seq_RNA=seq.upper().replace("T", "U")
    return seq_RNA

if __name__ == '__main__':
    with open("./data/rosalind_rna.txt") as input_data:
        seq=input_data.read().strip()
    print DNA_to_RNA(seq)