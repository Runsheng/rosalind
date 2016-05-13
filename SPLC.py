#!/usr/bin/env python
"""
Rosalind ID:SPLC
Problem Title:RNA Splicing
URL:http://rosalind.info/problems/splc/
2016/05/13, runsheng
todo: un
"""

from PROT import translate
from GC import fasta_to_dic

def splice(seq_full, seq_introns):
    """
    :param: seq_full should be a string
    :param: seq_introns should be a list of sub-strings inside seq_full
    :return the translated protein sequence
    """
    for seq in seq_introns:
        #print seq_full,seq
        try:
            start=seq_full.index(seq)
            end=start+len(seq)
            seq_full=seq_full[:start]+seq_full[end:]
        except ValueError:
            print ValueError
            print "Check the full length sequence contains the intron!"
    seq_exon=seq_full.replace("T", "U")
    return translate(seq_exon)

def get_longest(ref_dic):
    v_l=ref_dic.values()
    len_l=[len(x) for x in v_l]
    i=len_l.index(max(len_l))

    seq_full=v_l[i]
    v_l.pop(i)
    seq_introns=v_l

    return seq_full, seq_introns

if __name__=="__main__":
    ref_dic=fasta_to_dic("./data/rosalind_splc.txt")
    seq_full, seq_introns=get_longest(ref_dic)
    print splice(seq_full,seq_introns)
