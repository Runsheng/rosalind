#!/usr/bin/env python
'''
Rosalind ID: GRPH
Problem Title: Overlap Graphs
URL: http://rosalind.info/problems/grph/
2015/02/01, runsheng
'''

from GC import fasta_to_dic

def graph(seqs, k=3):
    """
    Given: A collection of DNA strings in FASTA format.
    Return: The adjacency list corresponding to O3(k=3). The format is tuples in list.
    Require function: fasta_to_dic() from GC
    """
    primer_5={}
    primer_3={}
    for name in seqs.keys():
        primer_5[name]=seqs[name][:k]
        primer_3[name]=seqs[name][-k:]
    overlap=[]
    for name_5 in primer_5.keys():
        for name_3 in primer_3.keys():
            if primer_5[name_5]==primer_3[name_3]:
                if name_5!=name_3:
                    overlap.append((name_3,name_5))
    return overlap

if __name__=="__main__":
    seqs=fasta_to_dic("./data/rosalind_grph.txt")
    for items in graph(seqs, k=3):
        print items[0],items[1]#,