#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import mul
import time

# https://projecteuler.net/problem=33

ITER = 100

def lists_overlap_once(a, b):
    return len(set(a).intersection(set(b))) == 1
     
def main():
    ans = []
    digits = [str(n) for n in range(11,ITER) if (n % 10) != 0]
    for n in digits:
        for d in digits:

            n_as_li = list(n)
            d_as_li = list(d)

            if lists_overlap_once(n_as_li, d_as_li):
                common_digit = list(set(n_as_li).intersection(set(d_as_li)))[0]
                product_both = float(n) / float(d)

                n_as_li.remove(common_digit)
                n_single_digit = n_as_li[0]

                d_as_li.remove(common_digit)
                d_single_digit = d_as_li[0]

                product_single = float(n_single_digit) / float(d_single_digit)

                if product_single < 1:
                    if product_single == product_both:
                        ans.append([n, d])

    li = []
    for a in ans:
        print a[0], a[1]
        li.append(float(a[0]) / float(a[1]))

    print li
    print reduce(mul, li)



if __name__ == '__main__':
    start_time = time.time()
    main()
    #print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 0.07 seconds
