#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=42


def main():

    f = file('042_words.txt')
    words = f.readlines()[0].replace('"','').split(',')
    print "words", words, len(words)


    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 11.20 seconds
