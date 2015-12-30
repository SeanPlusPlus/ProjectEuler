#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math
from collections import Counter

# https://projecteuler.net/problem=52

def get_hands():
    li = []
    f = file('p054_poker.txt','r')
    for line in f.readlines():
        li.append(line.strip().split(' '))
    return li

def compute(hand):
    pair = 0
    pair_card = None

    trips = False
    trips_card = None
    for k, v in hand.iteritems():
        if v == 2:
            pair += 1
            pair_card = k
        if v == 3:
            trips = True
            trips_card = k
    if pair == 1:
        if not trips:
            return {"pair_card": pair_card, "val": "pair"}
        else:
            return {"pair_card": pair_card, "trips_card": trips_card, "val": "full_house"}
    if pair == 2:
        return {"pair_card": pair_card, "val": "two_pair"}
    if trips:
        return {"trips_card": trips_card, "val": "trips"}

    return {"val": "high_card"}

def main():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    hands_list = get_hands()
    li = hands_list
    for el in li:
        player1 = []
        player2 = []
        for idx,card in enumerate(el):
            i = cards.index(card[0])
            if idx < 5: 
                player1.append(i)
            else:
                player2.append(i)

        target = "high_card"

        frequency = dict(Counter(player1))
        res = compute(frequency)
        if res.get("val") == target: 
            print player1, res

        frequency = dict(Counter(player2))
        res = compute(frequency)
        if res.get("val") == target: 
            print player2, res

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
