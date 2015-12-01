#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=15

###############################################################################
# 
# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
# 
# How I solved this in three steps:
# http://math.stackexchange.com/questions/103470/how-can-i-find-the-number-of-the-shortest-paths-between-two-points-on-a-2d-latti
# http://www.mathwords.com/b/binomial_coefficients.htm
# http://stackoverflow.com/questions/26560726/python-binomial-coefficient
#
###############################################################################

def main():
    grid = 20
    y = grid
    x = grid * 2
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x-y)
    div = a // (b * c)
    print(div) 

if __name__ == '__main__':
    main()
