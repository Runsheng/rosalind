#!/usr/bin/env python
'''
Rosalind #: 003
Rosalind ID: REVC
Problem Title: Complementing a Strand of DNA
URL: http://rosalind.info/problems/revc/
'''
def reverse_complement(seq):
    """
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    due to the complement_map,
    the symbol such as \n and something else is illegal
    the input need to be pure sequence
    """
    complement_map = dict(zip("acgtACGTNn-","tgcaTGCANn-"))
    complement=[]
    for s in seq:
        complement.append(complement_map[s])
    reverse=''.join(reversed(complement))
    return reverse

if __name__ == '__main__':
    with open("./data/rosalind_revc.txt") as input_data:
        seq=input_data.read().strip()
    print reverse_complement(seq)