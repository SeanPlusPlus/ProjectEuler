#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, operator, functools

# https://projecteuler.net/problem=48

def pow_reduce(n,k,i=2):
    n = (n * n) % int(math.pow(10,10))
    if i > k:
        return n
    i += 1
    return pow_reduce(n,k,i)

def get_exp(n,k):
    li = []
    b = "{0:b}".format(k)
    l = len(b) - 1
    for idx, digit in enumerate(b):
        if digit != "0":
            k = l - idx
            if k != 0:
                p = pow_reduce(n,k)
                li.append(p)
            else:
                li.append(n)
    ans = functools.reduce(operator.mul, li, 1)
    return ans % int(math.pow(10,10))

def main():
    li = [] 
    for num in range(1,1001):
        li.append(get_exp(num,num))
    print sum(li) % int(math.pow(10,10))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
