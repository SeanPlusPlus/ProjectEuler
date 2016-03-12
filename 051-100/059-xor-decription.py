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
    cipher = getCipherText()

    # the: 116, 104, 101
    triples = []
    the = [116, 104, 101]
    for j in range(97, 123):
        for k in range(97, 123):
            for l in range(97, 123):
                triples.append([the[0] ^ j, the[1] ^ k, the[2] ^ l])

    print triples

    # search cipher for instances of any triples occuring

if __name__ == '__main__':
    main()
