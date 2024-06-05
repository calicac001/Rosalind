"""
Complementing a strand of DNA

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other,
as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing
the symbols of s, then taking the complement of each symbol (e.g., the reverse
complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.
"""


def dna_complement(s):
    res = s.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T')
    res = res.replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')

    print(res[::-1])
