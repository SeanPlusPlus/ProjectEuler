#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=38

def concatenated_product(products):
    s = "".join([str(e) for e in products])
    return {
        "sorted_string": "".join(sorted( s )),
        "integer": int(s)
    }

def main():
    pan_digits_sorted_string = "".join([str(e) for e in range(1,10)])
    greatest = 0
    nums = range(1,10001)
    for num in nums:
        sequences = range(2,11)
        for s in sequences:
            products = []
            for i in range(1, s):
                products.append(i * num)
            product = concatenated_product(products) 
            if product["sorted_string"] == pan_digits_sorted_string:
                print "num:", num, "range: 1 ->", s, "product:", product["integer"]
                if product["integer"] > greatest:
                    greatest = product["integer"]

    print "greatest:", greatest

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.64 seconds
