#!/usr/bin/env python
'''
Rosalind ID: CONS
Problem Title: Consensus and Profile
URL: http://rosalind.info/problems/cons/
2015/02/01, runsheng
'''
from GC import fasta_to_dic
def con_matrix(fastafile):
    '''
    Given: reads in fasta format
    Return: a profile matrix for A,C,G,T
    Require function: fasta_to_dic() from GC
    '''
    seqs=fasta_to_dic(fastafile)
    for seq in seqs.values():
        len_seq=len(seq)
    A=[0]*len_seq
    C=[0]*len_seq
    G=[0]*len_seq
    T=[0]*len_seq
    for seq in seqs.values():
        for n in range(0,len(seq)):
            if seq[n]=="A":
                A[n]+=1
            if seq[n]=="C":
                C[n]+=1
            if seq[n]=="G":
                G[n]+=1
            if seq[n]=="T":
                T[n]+=1
    return A, C, G, T

def cons(A,C,G,T):
    """
    Given: four list contains the A,C,G,T frenqency
    Return: the consensus string of the matrix
    """
    cons_string=[]
    for i in range(0,len(A)):
        col={"A":A[i], "C":C[i], "G":G[i], "T":T[i]}
        max_n=max(col.values())
        #count=0
        for N in col.keys():
            if col[N]==max_n:
                cons_string.append(N)
                #just take the first as best
                break
                #count+=1
            #if count>1:
                #print "Dupilicated best!"
    return "".join(cons_string)

def cons_print(fastafile):
    """
    Use the con_matrix() and cons() function \
    to give a pretty output fitting the answer format
    """
    """
    with open("foo.txt","w") as f:
        A,C,G,T=con_matrix(fastafile)
        f.write(cons(A,C,G,T))
        f.write("\n")
        N_dict=dict(zip(["A","C","G","T"], (A,C,G,T)))
        for N in sorted(N_dict.keys()):
            f.write(str(N)+": "+(" ".join(str(i) for i in N_dict[N])))
            f.write("\n")
    """
    A,C,G,T=con_matrix(fastafile)
    print cons(A,C,G,T)
    N_dict=dict(zip(["A","C","G","T"], (A,C,G,T)))
    for N in sorted(N_dict.keys()):
        print (str(N)+": "+(" ".join(str(i) for i in N_dict[N])))


if __name__=="__main__":
    cons_print("./data/rosalind_cons.txt")