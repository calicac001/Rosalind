"""
Count Point Mutations

Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched
symbols are colored red.

Given two strings s and t of equal length, the Hamming distance between s
and t, denoted dH(s,t), is the number of corresponding symbols that differ in s
and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""


def hamm_dist(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)


"""
Alternative shorter solutions:
    1. ZIP function:
        print [ a!=b for (a, b) in zip(s1, s2)].count(True)
        or
        sum(a != b for a, b in zip(s1, s2))
        or
        sum(a != b for a, b in itertools.izip(s1, s2))
        
        - The zip() function returns a zip object, which is an iterator of 
        tuples where the first item in each passed iterator is paired together, 
        and then the second item in each passed iterator are paired together etc
        - sum() vs sum([]): first one sums as it goes along, but second one
        builds a list then sums list.
        - last option with itertools.izip saves memory by not making lists. It
        creates an iterator which means the list is not built, and instead a 
        function is returned, which gives you the tuples one-by-one, so you only
         ever have a single tuple in memory.
"""


