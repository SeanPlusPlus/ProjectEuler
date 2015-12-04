#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=42

def get_words():
    f = file('042_words.txt')
    words = f.readlines()[0].replace('"','').rstrip().split(',')
    return words

def triangle(n):
    return int((.5 * n) * (n + 1))

def main():
    triangles = [triangle(n) for n in range(1,1000)]
    letters = {}
    for idx, n in enumerate(range(65,91)):
        letters[chr(n)] = idx + 1

    words = get_words()
    triangle_words = 0
    for word in words:
        word_sum = 0
        for letter in word:
            word_sum += letters[letter]
        if word_sum in triangles:
            triangle_words += 1

    print triangle_words

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0 seconds
