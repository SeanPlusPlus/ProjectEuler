#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=31
# FULL DISCLOSUE: http://blog.dreamshire.com/project-euler-31-solution/
     
def main():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0 for n in range(target)]

    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]

    print "ways", ways[target]

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0 seconds
