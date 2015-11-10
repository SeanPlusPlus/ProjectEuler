#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://projecteuler.net/problem=14

###############################################################################
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#    Although it has not been proved yet (Collatz Problem), it is thought that all 
#    starting numbers finish at 1.
#
#    Which starting number, under one million, produces the longest chain?
#
#    NOTE: Once the chain starts the terms are allowed to go above one million.
# 
###############################################################################

def collatz(n, length):
    if n == 1:
        return length
    elif (n % 2) == 0:
        length += 1
        n = n / 2
        return collatz(n, length)
    else:
        length += 1
        n = (3 * n) + 1
        return collatz(n, length)

###############################################################################
def main():
###############################################################################

    starting_number = None
    longest_chain = 0
    for num in range(1, 1000000):
        chain_length = collatz(num, 1)
        if chain_length > longest_chain:
            print num
            print chain_length
            print ''
            longest_chain = chain_length
            starting_number = num

    print starting_number

###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
