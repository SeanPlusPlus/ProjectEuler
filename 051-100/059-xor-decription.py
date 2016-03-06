#!/usr/bin/env python

# https://projecteuler.net/problem=59

def nums():
    f = open('p059_cipher.txt')
    lines = f.readlines()[0]
    li = []
    for l in lines.split(','):
        li.append(int(l.strip('\n')))
    return li

def main():
    li = nums()
    print li
    print ord('A')
    print ord('*')
    print ord('k')

if __name__ == '__main__':
    main()
