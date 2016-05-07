#!/usr/bin/env python

def path_sum(li):
    try:
        new_base = []
        for idx, el in enumerate(li[-2]):
            new_base.append(el + max(li[-1][idx], li[-1][idx+1]))
        li[-2] = new_base
    except IndexError:
        return li[0][0]
    li.pop()
    return path_sum(li)

def main():

    example = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]

    # print path_sum(example)

    triangle = []
    f = open('./p067_triangle.txt')
    for line in f.readlines():
        triangle.append([int(el) for el in line.split(' ')])

    print path_sum(triangle)

if __name__ == '__main__':
    main()
