#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math
from collections import Counter
from itertools import groupby
from operator import itemgetter

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

    fours = False
    fours_card = None

    cards = []

    for k, v in hand.iteritems():
        cards.append(k)
        if v == 2:
            pair += 1
            pair_card = k
        if v == 3:
            trips = True
            trips_card = k
        if v == 4:
            fours = True
            fours_card = k

    # pair / full_house
    if pair == 1:
        if not trips:
            return {"card": pair_card, "val": "pair"}
        else:
            return {"pair_card": pair_card, "trips_card": trips_card, "val": "full_house"}

    # two_pair
    if pair == 2:
        return {"val": "two_pair"}

    # trips
    if trips:
        return {"card": trips_card, "val": "trips"}

    # fours
    if fours:
        return {"card": fours_card, "val": "fours"}

    # straight 
    cards.sort()
    for k, g in groupby(enumerate(cards), lambda (i, x): i-x):
        if len(map(itemgetter(1), g)) == 5:
            return {"val": "straight", "cards": cards}

    # high_card
    return {"val": "high_card", "card": max([k for k,v in hand.iteritems()])}

def main():
    wins = 0
    order = ["high_card", "pair", "two_pair", "trips", "straight", "flush", "full_house"]
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    hands_list = get_hands()
    li = hands_list
    for el in li:
        player1 = {'cards':[], 'flush': []}
        player2 = {'cards':[], 'flush': []}
        for idx,card in enumerate(el):
            i = cards.index(card[0])
            s = card[1]
            if idx < 5: 
                player1['cards'].append(i)
                player1['flush'].append(s)
            else:
                player2['cards'].append(i)
                player2['flush'].append(s)

        flush = False
        if len(set(player1['flush'])) == 1:
            flush = True
        player1['flush'] = flush

        flush = False
        if len(set(player2['flush'])) == 1:
            flush = True
        player2['flush'] = flush

        # target = "trips"

        frequency = dict(Counter(player1['cards']))
        res1 = compute(frequency)
        o1 = order.index(res1.get('val'))

        frequency = dict(Counter(player2['cards']))
        res2 = compute(frequency)
        o2 = order.index(res2.get('val'))


        if o2 > o1:
            continue

        if o1 > o2:
            wins += 1

        if o1 == o2:

            # not correct order on computing flush
            if player1['flush']:
                if not player2['flush']:
                    wins += 1

            elif player2['flush']:
                if not player1['flush']:
                    continue

            elif res1.get('card') > res2.get('card'):
                wins += 1

            elif res1.get('card') < res2.get('card'):
                continue

            else:
                pass

    print "wins", wins

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
