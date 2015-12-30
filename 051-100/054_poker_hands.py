#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math

# https://projecteuler.net/problem=52

def get_hands():
    li = []
    f = file('p054_poker.txt','r')
    for line in f.readlines():
        li.append(line.strip().split(' '))
    return li

def main():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K", "A"]
    hands = get_hands()
    print hands[0]

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
