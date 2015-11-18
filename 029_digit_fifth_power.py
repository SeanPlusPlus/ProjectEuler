#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from decimal import *

# https://projecteuler.net/problem=29

def main():
    ITER = 101
    s = set()
    with localcontext(Context(prec=201)) as ctx:
        for n in range(2,ITER):
            for exp in range(2,ITER):
                x = ctx.power(n,exp)
                print x
                s.add(x)
            print ''

    print 'distinct terms: \n', len(s)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

    # 0.53 seconds
