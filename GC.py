#!/usr/bin/env python
'''
Rosalind ID: GC
Problem Title: Computing GC Content
URL: http://rosalind.info/problems/gc/
2014/01/28, runsheng
'''
def fasta_to_dic(fastafile):
    '''
    Givin: a fasta file
    Return: a dic store the sequence
    '''
    seq_dic={}
    with open(fastafile,"r") as fa:
        lines=fa.readlines()
        for i in range(0,len(lines)):
            if lines[i][0]==">":
                name=lines[i].strip().replace(">", "")
                seq=[]
            else:
                seq.append(lines[i].strip())
            seq_dic[name]="".join(seq)
    return seq_dic

def gc_cal(seq_dic):
    """
    Givin: a fasta dic generated by fasta_to_dic()
    Return: a dic store the name and GC content
    """
    gc_dic={}
    for name in seq_dic.keys():
        seq=str(seq_dic[name]).upper()
        gc_count=0
        for i in seq:
            if i =="C" or i=="G":
                gc_count+=1
        gc_percent=float(gc_count)/len(seq)*100
        gc_dic[name]=gc_percent
    return gc_dic

def max_gc(gc_dic):
    """
    Givin: a dic with the name and GC content, generated by gc_cal()
    Return: no return, just print out the name and the GC content of the sequence with highest GC content
    """
    max_gc=max(list(gc_dic.values()))
    for name in gc_dic.keys():
        if gc_dic[name] ==max_gc:
            print name
            print gc_dic[name]
            #return name, gc_dic[name]

if __name__ == "__main__":
    seq_dic=fasta_to_dic("./data/rosalind_gc.txt")
    max_gc(gc_cal(seq_dic))