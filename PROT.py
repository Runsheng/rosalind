#!/usr/bin/env python
'''
Rosalind ID: PROT
Problem Title: Translating RNA into Protein
URL: http://rosalind.info/problems/prot/
2016/04/07, runsheng
'''

def translate(seq):
    """
    :param seq: An RNA string ss corresponding to a strand of mRNA.
    :return:The protein string encoded by ss.
    """
    codon="""
    UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G
    """
    codon_dict={}
    for line in codon.split("   "):
        if len(line)>=4:
            k,v=line.strip().split(" ")
            if v=="Stop":
                v="-"
            else:
                pass
            codon_dict[k]=v

    pro_l=[]
    print len(seq)
    for i in range(0,len(seq)):
        if (i+1)%3==0:
            pro_l.append(codon_dict[seq[(i-2):(i+1)].upper()])

    return "".join(pro_l).replace("-","")
if __name__=="__main__":
    with open("data/rosalind_prot.txt", "r") as f:
        seq=f.read()
    print translate(seq)
