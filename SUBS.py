#!/usr/bin/env python
'''
Rosalind ID: SUBS
Problem Title: Finding a Motif in DNA
URL: http://rosalind.info/problems/subs/
2015/01/31, runsheng
'''
def pattern_find(Text, Pattern):
    """
    Given: Two DNA strings s and t
    Return: All locations of t as a substring of s.
    """
    pos_list=[]
    for i in range (0,(len(Text)-len(Pattern))):
        if Text[i:(i+len(Pattern))] == Pattern:
            pos_list.append(i+1)
    return pos_list

if __name__=="__main__":
    with open("./data/rosalind_subs.txt") as subs:
        temp=subs.read().split("\n")
        Text=temp[0]
        Pattern=temp[1]
        for i in pattern_find(Text, Pattern):
            print i,