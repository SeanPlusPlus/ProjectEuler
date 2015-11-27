#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import string

# https://projecteuler.net/problem=36

def main():

    def is_palindrome(string):
        for i,char in enumerate(string):
            if char != string[-i-1]:
                return False
        return True

    digs = string.digits + string.letters
    def int2base(x, base):
        if x < 0: sign = -1
        elif x == 0: return digs[0]
        else: sign = 1
        x *= sign
        digits = []
        while x:
            digits.append(digs[x % base])
            x /= base
        if sign < 0:
            digits.append('-')
        digits.reverse()
        return ''.join(digits)

    ans = 0
    for n in range(0,1000001):
        n_str = str(n)
        n_bin = int2base(n,2)
        if is_palindrome(n_str):
            if is_palindrome(n_bin):
                print n, n_bin
                ans += n
    
    print "ans:", ans

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 290.45 seconds
