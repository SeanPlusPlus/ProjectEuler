#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=55

def flip(n):
    return int(str(n)[::-1])

def main():
    for n in range(10,21):
        print n, flip(n)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
