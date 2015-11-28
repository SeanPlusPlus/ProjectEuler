#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=38

def concatenated_product(products):
    return ''.join(sorted( ''.join([str(e) for e in products]) ))

def main():
    digits = ''.join([str(e) for e in range(1,10)])
    products = []
    for n in range(1,4):
        product = n * 192
        products.append(product)
    concatenated = concatenated_product(products)
    if concatenated == digits:
        print concatenated, digits

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 692.47 seconds
