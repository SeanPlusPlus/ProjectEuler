#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://projecteuler.net/problem=26

def cycles(n, d, start=0, steps=0):

    #print steps, n, d, start

    if d % 2 == 0: # d can not be even
        return steps
        
    if d % 3 == 0: # d can not be multiple of 3
        return steps

    if d % 5 == 0: # d can not be multiple of 3
        return steps

    steps += 1
    if steps == 1:
        start = 10 * (n % d)
        n = start
        return cycles(n, d, start, steps)

    n = 10 * (n % d)
    if n == start:
        return steps - 1

    return cycles(n, d, start, steps)
    
def main():

    n = 1
    largest = 0
    ans = 0
    for d in range(2,1000):
        c = cycles(n, d)
        if c > largest:
            largest = c
            ans = d
            
    print ans

if __name__ == '__main__':
    main()
