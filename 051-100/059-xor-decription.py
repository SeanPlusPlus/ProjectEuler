#!/usr/bin/env python

import itertools
import operator


def getCipherText():
    f = open('p059_cipher.txt')
    lines = f.readlines()[0]
    li = []
    for l in lines.split(','):
        li.append(int(l.strip('\n')))
    return li


def main():
    li = getCipherText()
    threshold = 6
    print [li[t] for t in range(threshold)]
    for i in range(97, 123):
        print chr(i), [chr(i ^ li[t]) for t in range(threshold)]


if __name__ == '__main__':
    main()
