#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

# https://projecteuler.net/problem=15
# HINT: http://cs.stackexchange.com/questions/37226/dynamic-programming-print-all-paths-from-0-0-to-n-n-in-grid-lattice

###############################################################################
# 
# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
###############################################################################

global n

def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

###############################################################################
def main():
###############################################################################

    @memo
    def f(i, j):
        if i > j:
            return []
        if not (0 <= i <= n and 0 <= j <= n):
            return []
        if i == n and j == n:
            return [[(n,n)]]
        alls = []
        for path in f(i, j+1)+f(i+1, j):
            if len(path) > 0:
                alls += [[(i,j)] + path] 
        return alls

    n = 2
    for path in f(0,0):
        print path

###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
