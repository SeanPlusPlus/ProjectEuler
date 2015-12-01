#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas

# https://projecteuler.net/problem=13

###############################################################################
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# 
# see 013_sum_big_num.csv
# 
###############################################################################

###################################################################################
def main():
###############################################################################

    sum_of_nums = 0
    data = pandas.read_csv('013_sum_big_num.csv', header=None)
    for row in data.values:
        sum_of_nums += int(row[0])

    print str(sum_of_nums)[0:10]



###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
