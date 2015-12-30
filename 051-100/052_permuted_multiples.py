#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math

# https://projecteuler.net/problem=52

def main():
    i = 142857
    for i in range(1,10000000):
        li = []
        for n in range(1,7):
            s = list(str(i * n))
            s.sort()
            li.append(''.join(s))
        if len(set(li)) == 1:
            print i 
            return

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
