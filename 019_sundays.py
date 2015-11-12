#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar

# https://projecteuler.net/problem=19

###############################################################################
# 
# You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
###############################################################################


def main():

    sundays_on_first_of_month = 0

    sunday = 6 # it is the last day of the week, with zero indexing
    for year in range(1901,2001):
        for month in range(1,13):
            if calendar.datetime.date(year,month,1).weekday() == sunday:
                sundays_on_first_of_month += 1

    print sundays_on_first_of_month

if __name__ == '__main__':
    main()
