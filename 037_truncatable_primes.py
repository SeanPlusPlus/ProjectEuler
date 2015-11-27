#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math

# https://projecteuler.net/problem=37
# you could just look here and sum, but that feels like cheating

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def trim_str(s, direction="left"):
    if direction == "left":
        trimmed = s[1:]
    else:
        trimmed = s[:-1]
    if len(trimmed) == 0:
        return True
    if not is_prime(int(trimmed)):
        return False
    return trim_str(trimmed, direction)

def primes():
    current = 10
    while True:
        current += 1
        while True:
            for i in xrange(2, current // 2 + 1):
                if current % i == 0:
                    current += 1
                    break
            else:
                break
        yield current

def main():
    truncatable_primes = []
    p = primes()

    while True:
        i = p.next()
        #print i
        s = str(i)
        if trim_str(s):
            if trim_str(s, direction="right"):
                print i
                truncatable_primes.append(i)
        if len(truncatable_primes) == 11:
            break

    print "sum truncatable_primes:", sum(truncatable_primes)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 692.47 seconds
