#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, itertools

# https://projecteuler.net/problem=48

def get_prime_perms(li):
    intersection = {}
    diffs = []
    for idx, el in enumerate(li):
        # print idx, el
        li1 = []
        li2 = []
        for i in range(idx+1,len(li)):
            n = li[i] - li[idx]
            # print i, ":", n, ":", n * 2
            li1.append(n)
            li2.append(n*2)
            diffs.append(li[i] - li[idx])
        ans = set.intersection(set(li1), set(li2))
        if len(ans) > 0:
            intersection['difference'] = next(iter(ans)) / 2
    if len(diffs)!=len(set(diffs)):
        if 'difference' in intersection:
            print intersection, li

def get_4_digit_primes(limit):
    a = [True] * limit 
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def main():
    p = get_4_digit_primes(100000)
    primes = []
    for n in range(1250):
        prime = p.next()
        if prime > 999 and prime < 10000:
            primes.append(prime)

    #p = str(primes[0])
    #ps = ["1487", "1009"]
    ps = primes
    for p in ps:
        perm_list = []
        for n in itertools.permutations(str(p)): 
            num = int(''.join(n))
            if num > 999 and num < 10000:
                perm_list.append(num)

        prime_perms = []
        li = list(set(perm_list))
        li.sort()
        for perm in li:
            if perm in primes:
                prime_perms.append(perm)
        if len(prime_perms) > 2:
            get_prime_perms(prime_perms)

    # [3947, 4397, 4793, 4937, 4973, 7349, 9437, 9473, 9743]


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
