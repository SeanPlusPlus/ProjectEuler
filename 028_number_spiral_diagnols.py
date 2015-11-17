#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import cycle

# https://projecteuler.net/problem=28
# FULL DISCLOSURE: http://stackoverflow.com/questions/23706690/how-do-i-make-make-spiral-in-python

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

def main():
    li = list(gen_points(9))
    for el in li:
        print el


if __name__ == '__main__':
    main()
