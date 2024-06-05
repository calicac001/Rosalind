"""
Counting DNA Nucleotides

Problem
A string is simply an ordered collection of symbols selected from some alphabet
and formed into a word; the length of a string is the number of symbols that it
contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A',
'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""


def count_nuc_v1(s):
    nucleotides = ['A', 'C', 'G', 'T']
    count = [0, 0, 0, 0]

    for ch in s:
        for i in range(len(nucleotides)):
            if ch == nucleotides[i]:
                count[i] += 1

    print(' '.join(str(c) for c in count))


def count_nuc_v2(s):
    print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))
