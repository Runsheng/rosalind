#!/usr/bin/env python
'''
Rosalind ID: IEV
Problem Title: Calculating Expected Offspring, The Need for Averages
URL: http://rosalind.info/problems/iev/
2016/04/07, runsheng

 uniform random variable
 E(X)=min+max/2
'''

def dom_prob(int_string):
    """
    :param int_string:Six positive integers,
    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa
    :return:The expected number of offspring displaying the dominant phenotype
    """
    line_l=[int(i) for i in int_string.strip().split(" ")]

    sum=(line_l[0]*1.0+line_l[1]*1.0+line_l[2]*1.0+line_l[3]*0.75+
         line_l[4]*0.5)*2

    return sum

if __name__=="__main__":
    print dom_prob("18714 18996 19214 17047 18714 161905")

