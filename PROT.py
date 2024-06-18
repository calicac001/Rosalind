"""
Translating RNA into Protein

Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from
the English alphabet (all letters except for B, J, O, U, X, and Z). Protein
strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (length at most 10 kbp)

Return: The protein string encoded by s
"""

with open("datasets/codon.txt", "r") as file:
    data = file.readlines()

codon_table = {}
for line in data:
    pairs = line.rstrip().split("      ")
    for pair in pairs:
        p = pair.split(" ")
        codon_table[p[0]] = p[1]


def rna_to_prot(s):
    # split input string to codons
    codons = [s[i:i+3] for i in range(0, len(s), 3)]
    protein = ""

    for c in codons:
        if codon_table[c] != "Stop":
            protein += codon_table[c]
    print(protein)


rna_to_prot("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
# output: MAMAPRTEINSTRING
