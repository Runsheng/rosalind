#!/usr/bin/env python
'''
Rosalind ID: LCSM
Problem Title: Finding a Shared Motif
URL: http://rosalind.info/problems/lcsm/
2016/04/07, runsheng
'''

from GC import fasta_to_dic

def common(fastafile):
    """
    :param fastafile: fasta seq file
    :return:A longest common substring of the fasta sequences
    """
    fa_dic=fasta_to_dic(fastafile)
    fa_seq_0=fa_dic.values()[0] # select the first read as seed

    seq_len=len(fa_seq_0)
    for k in reversed(range(seq_len)):
        for i in range(0,seq_len-k):
            kmer=fa_seq_0[i:(i+k)]
            for key in fa_dic.keys():
                if kmer not in fa_dic[key]:
                    break
                elif key==fa_dic.keys()[-1] and kmer in fa_dic[key]:
                    return kmer  # only return the fist one

    return None

if __name__=="__main__":
    print common("./data/rosalind_lcsm.txt")

