#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=38

def concatenated_product(products):
    s = ''.join([str(e) for e in products])
    return {
        "sorted": ''.join(sorted( s )),
        "raw": int(s)
    }

def main():
    digits = ''.join([str(e) for e in range(1,10)])

    products = []
    target = 192
    r = [1,4]
    for i in range(r[0],r[1]):
        product = i * target
        products.append(product)
    concatenated = concatenated_product(products) 
    if concatenated['sorted'] == digits:
        print target, concatenated

    products = []
    target = 9
    r = [1,6]
    for i in range(r[0],r[1]):
        product = i * target
        products.append(product)
    concatenated = concatenated_product(products) 
    if concatenated['sorted'] == digits:
        print target, concatenated

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0 seconds
