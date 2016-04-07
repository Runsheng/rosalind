#!/usr/bin/env python
'''
Rosalind ID: IPRB
Problem Title: Introduction to Mendelian Inheritance
URL: http://rosalind.info/problems/iprb/
2016/04/07, runsheng
'''


def dom_prob(k,m,n):
    """
    3 positive integers k, m, and n, representing a population containing k+m+nk+m+n organisms
    :param k: k individuals are homozygous dominant for a factor
    :param m: m are heterozygous
    :param n: n are homozygous recessive
    :return:The probability that two randomly selected
            mating organisms will produce an individual possessing a dominant allele
    """
    #  whole offspring possibility
    # be aware of the float and divide in python2
    # C(sum,2)
    no_sum=(k+m+n)*(k+m+n-1)/2.0

    # 1/4*C(m,2)+1/2*C(m,1)*C(n,1)+C(n,2)
    no_res=0.25*m*(m-1.0)/2.0+0.5*n*m +n*(n-1.0)/2.0
    # sanity check
    print "The total number is {0} and dominant number is {1}".format(no_sum,no_res)

    return float(no_sum-no_res)/no_sum


if __name__=="__main__":
    with open("./data/rosalind_iprb.txt") as f:
        for line in f.readlines():
            k,m,n=line.strip().split(" ")
            print "k,m,n is ", k,m,n
    print dom_prob(int(k),int(m),int(n))