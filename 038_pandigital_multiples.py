#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=38

def concatenated_product(products):
    s = "".join([str(e) for e in products])
    return {
        "sorted": "".join(sorted( s )),
        "raw": int(s)
    }

def main():
    pan_digits_sorted = "".join([str(e) for e in range(1,10)])
    greatest = 0
    targets = range(1,10001)
    for target in targets:
        sequences = range(2,11)
        for s in sequences:
            products  = []
            for i in range(1, s):
                product = i * target
                products.append(product)
            concatenated = concatenated_product(products) 
            if concatenated["sorted"] == pan_digits_sorted:
                print "taget:", target, "range bound:", s, "product:", concatenated["raw"]
                if concatenated["raw"] > greatest:
                    greatest = concatenated["raw"]

    print "greatest:", greatest

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.64 seconds
