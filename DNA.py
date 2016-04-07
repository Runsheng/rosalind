#!/usr/bin/env python
'''
Rosalind #: 001
Rosalind ID: DNA
Problem Title: Counting DNA Nucleotides
URL: http://rosalind.info/problems/dna/
'''
def count_DNA(seq):
    '''
    input: the sequence input as a string
    return: the number of A,C,G,T in a set
    '''
    a,c,g,t=0,0,0,0
    for nucl in seq:
        if nucl=="A":
            a+=1
        if nucl=="C":
            c+=1
        if nucl=="G":
            g+=1
        if nucl=="T":
            t+=1
    return "%s %s %s %s" % (a,c,g,t)

def main():
    with open("./data/rosalind_dna.txt") as input_data:
        seq=input_data.read().strip()
    print count_DNA(seq)

if __name__ == '__main__':
    main()