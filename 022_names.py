#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import string

# https://projecteuler.net/problem=22

def getNames():

    f = open('022_names.txt')
    for line in f:
        li = line

    names = []
    for el in li.split(','):
        names.append(el[1:-1])

    names.sort()
    return names

def getScore(pos, name):
    name_val = 0
    for c in name:
        print c
        name_val += int(string.lowercase.index(c.lower())) + 1
        print name_val

    return name_val * (pos)
    
def main():

    names = getNames()

    name_scores = 0
    for idx, n in enumerate(names):
        name_scores += getScore( idx+1, n)

    print name_scores

if __name__ == '__main__':
    main()
