"""
Mortal Fibonacci Rabbits

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 nd assumed that
each pair of rabbits reaches maturity in one month and produces a single pair of
 offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed number
of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.
"""
from functools import lru_cache

# Recursive Approach
@lru_cache(None)
def rabbit_pairs(n: int, m: int):
    if n <= 2:
        return 1
    else:
        if n > m:
            # both work but bottom one requires less calculation
            # return sum(rabbit_pairs(n-x, m) for x in range(2, m+1))

            # sum the rabbits born in the last m-1 months subtracting
            # those that die
            return rabbit_pairs(n-1, m) + rabbit_pairs(n-2, m) - rabbit_pairs(n-m-1, m)
        else:
            return rabbit_pairs(n-1, m) + rabbit_pairs(n-2, m)


# Dynamic Programming appraoch
def dp_mfr(n: int, m: int):
    # Initialize array to hold the number of rabbits at each month
    rabbits = [0]*(n+1)
    # Base Case
    rabbits[1] = 1

    for month in range(2, n + 1):
        if month <= m:
            # sum the rabbits born in last n-1 months
            rabbits[month] = rabbits[month - 1] + rabbits[month - 2]
        else:
            # Sum the rabbits born in the last m-1 months, subtract those that
            # die this month
            rabbits[month] = rabbits[month - 1] + rabbits[month - 2] \
                             - rabbits[month - m - 1]

    # return number of rabbits alive at month m
    return rabbits[m]


if __name__ == "__main__":
    ans = rabbit_pairs(96, 18)
    print(ans)
