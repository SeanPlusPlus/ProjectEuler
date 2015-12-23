#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math

# https://projecteuler.net/problem=48

def pow_reduce(n,k, count=0):
    count += 1
    n = (n * n) % 100
    b = "{0:b}".format(n)
    print "n:", n, "b:", b, "len b:", len(b)
    if count == k:
        print n
        return n
    return pow_reduce(n,k,count)


def main():
    num = 2
    exp = 4
    pow_reduce(num,exp)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
