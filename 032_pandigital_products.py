#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools as it
import time

# https://projecteuler.net/problem=32

ITER = 10
     
def main():
    digits = set([str(n) for n in range(1,ITER)])
    products = set()

    pairs = [[2,3],[1,4]]
    for number in pairs:
        multipliers = it.permutations(digits,number[0])
        for multiplier in multipliers:
            li = list(digits - set(multiplier))
            multiplicands = it.permutations(li,number[1])
            for multiplicand in multiplicands:
                a = int(''.join(multiplier))
                b = int(''.join(multiplicand))
                product = a * b
                product_tuple = tuple(str(product))
                if len(product_tuple) == 4:
                    s = set(multiplier + multiplicand + tuple(str(product)))
                    if len(s) == 9:
                        if '0' not in s:
                            print a,b,product,s 
                            products.add(product)

    print products
    print sum(products)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.07 seconds
