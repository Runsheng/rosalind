#!/usr/bin/env python
'''
Rosalind ID: LONG
Problem Title: Genome Assembly as Shortest Superstring
URL: http://rosalind.info/problems/long/
2015/04/17, runsheng

todo: unfinished
'''
# reqire: fasta2dic from GC

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

def graph(fastafile, k=3):
    """
    Given: A collection of DNA strings in FASTA format.
    Return: The adjacency list corresponding to O3(k=3). The format is tuples in list.
    Require function: fasta_to_dic() from GC
    """
    seqs=fasta_to_dic(fastafile)
    primer_5={}
    primer_3={}
    for name in seqs.keys():
        primer_5[name]=seqs[name][:k]
        primer_3[name]=seqs[name][-k:]
    overlap=[]
    for name_5 in primer_5.keys():
        for name_3 in primer_3.keys():
            if primer_5[name_5]==primer_3[name_3]:
                if name_5!=name_3:
                    overlap.append((name_3,name_5))
    return overlap

def get_shortest_superstring(fasta_records):
    adjacent_matrix = get_adjacent_matrix(fasta_records)
    assembly_chain = get_assembly_chain(adjacent_matrix)
    return glue(fasta_records, assembly_chain)

def get_adjacent_matrix(fasta_records):
    num_vertex = len(fasta_records)
    return [[is_adjacent(fasta_records[x][1], fasta_records[y][1])
        for y in range(num_vertex)] for x in range(num_vertex)]

def is_adjacent(u, v):
    """
    overlap by more than half their length
    can only be used in this assembler
    """
    for i in range(len(u)//2):
        j = len(u) - i
        if u[i:] == v[:j] and j > len(v)//2:
            return True
    return False

def get_assembly_chain(adjacent_matrix):
    num_vertex = len(adjacent_matrix)
    reversed_chain = [get_final_vertex(adjacent_matrix)]
    while len(reversed_chain) != num_vertex:
        last_vertex = reversed_chain[-1]
        for i in range(num_vertex):
            if adjacent_matrix[i][last_vertex] is True and i != last_vertex:
                reversed_chain.append(i)
                break
    return reversed_chain[::-1]

def get_final_vertex(adjacent_matrix):
    num_vertex = len(adjacent_matrix)
    final_vertex_list = [i for i in range(num_vertex)
        if adjacent_matrix[i].count(False) == num_vertex - 1]
    assert(len(final_vertex_list) == 1)
    return final_vertex_list[0]

def glue(fasta_records, assembly_chain):
    superstring = fasta_records[assembly_chain[0]][1]
    num_vertex = len(fasta_records)
    for i in range(1, num_vertex):
        prev_vertex = fasta_records[assembly_chain[i-1]][1]
        curr_vertex = fasta_records[assembly_chain[i]][1]
        for j in range(len(curr_vertex), 0, -1):
            if curr_vertex[:j] == prev_vertex[len(prev_vertex) - j:]:
                superstring += curr_vertex[j:]
                break
    return superstring

def main():
    fasta_records = get_fasta_records(sys.stdin.readlines())
    print(get_shortest_superstring(fasta_records))

if __name__ == '__main__':
    sys.exit(main())

def assembly(fastafile):
    """
    Given: At most 50 DNA strings whose length does not exceed 1 kbp in
    FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
    The dataset is guaranteed to satisfy the following condition:
    there exists a unique way to reconstruct the entire chromosome from these reads by gluing
    together pairs of reads that overlap by more than half their length.

    Return: A shortest superstring containing all the given strings
    (thus corresponding to a reconstructed chromosome).

    Require: graph() function in GRAPH，fasta_to_dic() function in GC
    """
    overlap_list=graph(fastafile, k=300)