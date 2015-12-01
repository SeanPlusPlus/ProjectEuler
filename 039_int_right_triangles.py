#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools
import operator

# https://projecteuler.net/problem=39

def most_common(L):
    # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(L))
    # print 'SL:', SL
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]

def trips(max_value):
    li = []
    for a in range(1, max_value):
        for b in range(a, max_value):
            for c in range(b, max_value):
                if a**2 + b**2 == c**2:
                    print a,b,c
                    li.append(a+b+c)
    return li

def main():
    li = trips(500)
    print "most common:", most_common(li)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.64 seconds
