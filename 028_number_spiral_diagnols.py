#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from itertools import cycle

# https://projecteuler.net/problem=28
# how to generate spiral: 
# http://stackoverflow.com/questions/23706690/how-do-i-make-make-spiral-in-python

def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

def gen_points(end):
    moves = [move_right, move_down, move_left, move_up]

    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    yield n,pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n+=1
                yield n,pos

        times_to_move+=1

def get_diaganol(li, idx_x, idx_y):
    idx = 1
    res = []
    for el in li:
        x = el[1][0]
        y = el[1][1]
        if x == (idx * idx_x) and y == (idx * idx_y):
            res.append(el[0])
            idx += 1
    return res

def main():

    # build the spiral
    SIDE = 1001
    SPIRAL = SIDE * SIDE

    # generate list of tuples
    li = list(gen_points(SPIRAL))

    # walk out in each of four directions
    north_east = get_diaganol(li,  1,  1)
    south_east = get_diaganol(li, -1, -1)
    north_west = get_diaganol(li, -1,  1)
    south_west = get_diaganol(li,  1, -1)
    ans = north_east + south_east + north_west + south_west
    
    # yo!
    print sum(ans) + 1

if __name__ == '__main__':
    main()
