#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools
from operator import mul

# https://projecteuler.net/problem=40
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def main():
    expression = [1, 10, 100, 1000, 10000, 100000, 1000000]
    values = []
    digits = ''
    for i in itertools.count(start=1):
        digits += str(i)
        if i == expression[0]:
            print i, len(digits)
            values.append(int(digits[i-1]))
            expression.pop(0)
        if len(expression) == 0:
            print values
            print "ans:", reduce(mul, values, 1)
            return


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.64 seconds
