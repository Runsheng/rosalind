#!/usr/bin/env python
'''
Rosalind ID: FIBD
Problem Title: Mortal Fibonacci Rabbits
URL: http://rosalind.info/problems/fibd/
2015/01/31, runsheng
'''
known={0:0,1:1}
def fib(m):
    """generate a new end for fibd(n,m)"""
    if m in known:
        return known[m]
    res=fib(m-1)+fib(m-2)
    known[m]=res
    global known_new
    known_new=known
    return res

def fibd(n,m):
    """
    Given: Positive integers n≤100 and m≤20.
    Return: The total number of pairs of rabbits that will remain \
            after the n-th month if all rabbits live for m months.
    """
    if n in known_new:
        return known_new[n]
    res=fibd(n-1,m)+fibd(n-2,m)-fibd(n-1-m,m)
    known_new[n]=res
    #print res
    return res

def fibd_wrap(n,m=1):
    known={0:0,1:1}
    fib(m)
    # consider a speacial situation, n-(m+1)=0, the time first rabbit dies,\
    # this is needed in the new end and can not be generated by Recursion code
    k=m+1
    global known_new
    known_new[k]=known_new[k-2]+known_new[k-1]-1
    #print known_new #print the generated start of the recursions
    ###
    result=fibd(n,m)
    return result

#here is some others' solution in rosalind
def abeliangrape_fib(n,k=1):
    ages = [1] + [0]*(k-1)
    for i in xrange(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
        print ages
    return sum(ages)

def population(n, m=1):
    h = [0]*(m-2) + [1, 1, 1]
    for i in xrange(n-2):
        h += [h[-1] + h[-2] - h[-m-1]]
        #h = h[1:] + [h[-1] + h[-2] - h[0]] # even faster
    return h[-1]

if __name__=="__main__":
    import time
    start= time.clock()
    print fibd_wrap(6,3)
    end= time.clock()
    print "time1", end-start

    start= time.clock()
    print abeliangrape_fib(6,3)
    end= time.clock()
    print "time2", end-start

    start= time.clock()
    print population(6,3)
    end= time.clock()
    print "time3", end-start