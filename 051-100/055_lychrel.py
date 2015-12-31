#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=55

def is_palindrome(n):
    if n == flip(n):
        return True
    return False

def flip(n):
    return int(str(n)[::-1])

def lychrel(n, iterations=0):
    if iterations == 50:
        return False
    x = n + flip(n)
    if not is_palindrome(x):
        iterations += 1
        return lychrel(x, iterations)
    return True

def main():
    i = 0
    for n in range(10001):
        if not lychrel(n):
            i += 1
    print i

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
