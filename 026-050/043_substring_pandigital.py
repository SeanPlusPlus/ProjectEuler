#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, itertools

# https://projecteuler.net/problem=43

def main():
    primes = [2, 3, 5, 7, 11, 13, 17]
    li = []

    pan_digitals = "".join([str(n) for n in range(0,10)])
    for digits in itertools.permutations(pan_digitals):
        if digits[0] == '0':
            continue
        num = int(''.join(digits))
        flag = True
        for i in range(2,len(primes) + 2):
            s = ""
            n = str(num) 
            s += n[i-1]
            s += n[i]
            s += n[i+1]
            if (int(s) % primes[i-2]) != 0:
                flag = False
        if flag:
            print num
            li.append(int(num))

    print sum(li)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 102.81 seconds
