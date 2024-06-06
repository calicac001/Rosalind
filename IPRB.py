"""
Probability is the mathematical study of randomly occurring phenomena. We will
model such a phenomenon with a random variable, which is simply a variable that
can take a number of different distinct outcomes depending on the result of an
underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If
we let X represent the random variable corresponding to the color of a drawn
ball, then the probability of each of the two outcomes is given by Pr(X=red)=3/5
and Pr(X=blue)=2/5.

Random variables can be combined to yield new random variables. Returning to the
ball example, let Y model the color of a second ball drawn from the bag
(without replacing the first ball). The probability of Y being red depends on
whether the first ball was red or blue. To represent all outcomes of X and Y, we
therefore use a probability tree diagram. This branching diagram represents all
possible individual probabilities for X and Y, with outcomes at the endpoints (
"leaves") of the tree. The probability of any outcome is given by the product of
 probabilities along the path from the beginning of the tree    .

An event is simply a collection of outcomes. Because outcomes are distinct, the \
probability of an event can be written as the sum of the probabilities of its
constituent outcomes. For our colored ball example, let A be the event "Y is
blue." Pr(A) is equal to the sum of the probabilities of two different outcomes:
Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 3/10+1/10=2/5
(see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing
 k+m+n organisms: k individuals are homozygous dominant for a factor, m are
 heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce
 an individual possessing a dominant allele (and thus displaying the dominant
 phenotype). Assume that any two organisms can mate.
"""


"""
To produce individual with dominant allele, need ff. events:
    - AA x AA, 100% AA
    - AA x Aa, 100% with dominant allele (50% AA, 50% Aa) 
    - AA x aa, 100% Aa
    - Aa x Aa, 75% AA + Aa (25% aa)
    - Aa x aa, 50% Aa (other 50% aa)
    - aa x aa, 0%
"""


def mating_prb(k, m, n):
    total = k+m+n
    AAxAA = k/total * (k-1)/(total-1)
    AaxAa = (m/total * (m-1)/(total-1))*0.75

    # Also have to consider the order
    AAxAa = k/total * m/(total-1)
    AaxAA = m/total * k/(total-1)

    AAxaa = k/total * n/(total-1)
    aaxAA = n/total * k/(total-1)

    Aaxaa = (m/total * n/(total-1))*0.5
    aaxAa = (n/total * m/(total-1))*0.5

    print(AAxAA+AAxAa+AAxaa+AaxAa+Aaxaa+AaxAA+aaxAA+aaxAa)

"""
Alternative Solution is to calculate the recessives instead.
    - totally forgot about this!
    - i remember doing this in HMB265.
"""


def mating_prb_v2(k, m, n):
    total = k+m+n
    AaxAa = (m/total * (m-1)/(total-1))*0.25
    Aaxaa = (m/total * n/(total-1))*0.50
    aaxAa = (n/total * m/(total-1))*0.50
    aaxaa = n/total * (n-1)/(total-1)

    print(1 - (Aaxaa+AaxAa+aaxaa+aaxAa))

    # N = float(k+m+n)
    # return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )

if __name__ == "__main__":
    mating_prb_v2(23, 19, 20)
