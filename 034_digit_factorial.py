#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=34

def factorial(n):
    return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def digitStr(li):
    return ''.join(str(e) for e in li)

def digitList(i):
    return [int(el) for el in list(str(i))]

def numFromList(li):
    i = 0
    i += int(''.join(str(e) for e in li))
    return i

def main():

    c = []

    for n in range(1,100000):
        a = digitList(n)
        b = []
        for el in a:
            b.append(factorial(el))

        if digitStr(a) == str(sum(b)):
            c.append(a)

    ans = 0
    for el in c:
        if len(el) > 1:
            ans += numFromList(el)

    print "ans: ", ans

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.00 seconds
