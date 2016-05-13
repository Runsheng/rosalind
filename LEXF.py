#!/usr/bin/env python
"""
Rosalind ID:LEXF
Problem Title: Enumerating k-mers Lexicographically
URL:http://rosalind.info/problems/lexf/
2016/04/20, runsheng
"""

from itertools import product

def lexf(strs,k):
    return product(strs,repeat=k)

def test(strs,k):
    aa= lexf(strs,k)
    for i in aa:
        print "".join(i)

if __name__=="__main__":
    test("SADBMLWOZT", 2)

