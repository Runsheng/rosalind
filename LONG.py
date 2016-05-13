#!/usr/bin/env python
'''
Rosalind ID: LONG
Problem Title: Genome Assembly as Shortest Superstring
URL: http://rosalind.info/problems/long/
2015/04/17, runsheng
'''
"""
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

"""

# reqire: fasta2dic from GC
from GC import fasta_to_dic
from GRPH import graph

def find_startnode(overlap_d):
    """
    :param overlap_d:
    :return:
    """
    list_3=[]
    for v in overlap_d.values():
        list_3.append(v.keys()[0])

    for key in overlap_d.keys():
        if key not in list_3:
            start_node=key
    return start_node


def layout(overlap_d):
    overlap=[]
    start_node=find_startnode(overlap_d)
    print start_node
    overlap.append(start_node)

    for i in range(len(overlap_d)):
        overlap.append(overlap_d[overlap[-1]].keys()[0])
    print len(overlap)
    return overlap

def overlap(fa_dic, k_start=3):
    """
    :param fa_dic: fasta sequence dict
    :return: overlap_d: dict as {node1:{node2:length},...}
    """
    overlap_d={}
    # only add the best overlap node to set
    for k in range(k_start, len(fa_dic.values()[0])):
        overlap=graph(fa_dic, k)
        for pair in overlap:
            overlap_d[pair[0]]={pair[1]:k}
    print overlap_d
    return overlap_d

def _read_merge(primer_5, primer_3, k_start):
    """
    merge two sequence with unknown overlap
    :param primer_5:
    :param primer_3:
    :param k_start:
    :return:
    """
    for k in range(k_start, min(len(primer_5), len(primer_3))):
        if primer_5[-k:]==primer_3[:k]:
            pass
        else:
            return primer_5+primer_3[k-1:]


def read_merge(primer_5,primer_3,k):
    """
    merge two sequences with known overlap length
    :param primer_5:
    :param primer_3:
    :param k:
    :return:
    """
    return primer_5+primer_3[k:]


def assembly(fastafile, k_start=3):
    fa_dic=fasta_to_dic(fastafile)

    # init a dict for overlap graph, with weight as k
    overlap_d=overlap(fa_dic, k_start)
    read_order=layout(overlap_d)
    contig=""

    for n,name in enumerate(read_order):
        if n==0:
            contig0=fa_dic[name]
            contig=read_merge(contig0, fa_dic[read_order[n+1]], overlap_d[read_order[0]].values()[0])
        else:
            try:
                contig=read_merge(contig, fa_dic[read_order[n+1]], overlap_d[read_order[n]].values()[0])
            except IndexError:
                break
    return contig

if __name__=="__main__":
    # test using long_test.txt and k=4
    #print assembly("./data/long_test.txt", k_start=3)
    print assembly("./data/rosalind_long.txt", k_start=200)
