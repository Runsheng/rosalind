#!/usr/bin/env python
'''
Rosalind ID: FIB
Problem Title: Rabbits and Recurrence Relations
URL: http://rosalind.info/problems/fib/
2014/01/27, runsheng
'''
def fib(n, k):
    """
    Given: Positive integers n≤40 and k≤5.
    Return: The No. n element of Fibonacci sequence, \
    with the coefficient k (k=1 is the typic Fibonacci sequence, k=2 means one rabbit give birth to \
    2 samll rabits.)
    """
    #the recursive code need an end
    if n==1 or n==2:
        return 1
    else:
        return fib(n-2,k)*k+fib(n-1,k)


known={1:1,2:1}
def fib_dic(n,k):
    """
    Given: Positive integers n≤40 and k≤5.
    Return: The No. n element of Fibonacci sequence, with the coefficient k \
    (k=1 is the typic Fibonacci sequence, k=2 means one rabbit give birth to \
    2 samll rabits.)
    Store the cuculated data in a dict to make it faster, so called "memo" method
    """
    if n in known:
        return known[n]

    res= fib_dic(n-1,k)+fib_dic(n-2,k)*k
    known[n]=res
    return res

if __name__ == '__main__':
    import time
    start=time.clock()
    print fib(32,4)
    end=time.clock()
    print "fib cost " + str(end-start) + "s"

    start=time.clock()
    print fib_dic(32,4)
    end=time.clock()
    print "fib_dic cost " + str(end-start) + "s"