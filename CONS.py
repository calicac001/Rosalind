"""
Problem:

A matrix is a rectangular table of values divided into rows and columns. An m×n
matrix has m rows and n columns. Given a matrix A we write Ai,j to indicate the
value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number of
times that 'A' occurs in the jth position of one of the strings, P2,j represents
the number of times that C occurs in the jth position, and so on.

A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jh symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol,
leading to multiple possible consensus strings.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
"""


def print_consensus(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()

    nucleotides = ["A", "C", "G", "T"]

    dna_matrix = []
    
    for i in range(len(data)):
        if data[i].startswith(">"):
            dna_matrix.append("")
        else:
            dna_matrix[len(dna_matrix)-1] += data[i].rstrip("\n")

    # initialize profile with all zero values
    profile = {}
    for i in nucleotides:
        profile[i] = [0 for i in range(len(dna_matrix[0]))]

    # count instance of each nucleotide
    for i in range(len(dna_matrix)):
        for j in range(len(dna_matrix[i])):
            profile[dna_matrix[i][j]][j] += 1

    # determine consensus nucleotide per position
    consensus = []
    for i in range(len(dna_matrix[0])):
        max_nuc = ""
        num = 0
        for nuc in nucleotides:
            if profile[nuc][i] > num:
                num = profile[nuc][i]
                max_nuc = nuc
        consensus.append(max_nuc)

    # print consensus sequence
    print("".join(consensus))

    # print profile
    for nuc in profile:
        print(nuc + ": " + " ".join(str(x) for x in profile[nuc]))


print_consensus("datasets/input.txt")
