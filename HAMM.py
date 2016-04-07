#!/usr/bin/env python
'''
Rosalind ID: HAMM
Problem Title: Counting Point Mutations
URL: http://rosalind.info/problems/hamm/
2015/01/31, runsheng
'''
def hamm(s,t):
    """
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    """
    count=0
    for n in range(0,len(s)):
        if s[n]!=t[n]:
            count+=1
    return count

if __name__=="__main__":
    with open("./data/rosalind_hamm.txt") as sequence:
        seq=sequence.read().split("\n")
        s=seq[0]
        t=seq[1]
        print hamm(s,t)