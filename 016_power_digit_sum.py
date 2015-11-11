#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=16

###############################################################################
# 
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
#
###############################################################################

def main():

    sum_of_digits = 0
    for char in str(int(math.pow(2,1000))):
        sum_of_digits += int(char)
    print sum_of_digits

if __name__ == '__main__':
    main()
