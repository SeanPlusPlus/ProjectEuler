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


        res1 = compute(dict(Counter(player1['cards'])))
        o1 = order.index(res1.get('val'))
        if player1.get('flush') == True:
            o1 = 5

        res2 = compute(dict(Counter(player2['cards'])))
        o2 = order.index(res2.get('val'))
        if player2.get('flush') == True:
            o2 = 5

        if o1 > o2:
            wins += 1
            continue
        elif o2 > o1:
            continue
        elif (res1.get('val') == 'high_card') and (res2.get('val') == 'high_card'):
            if res1['card'] > res2['card']:
                wins +=1 
                continue
            else:
                continue
        elif (res1.get('val') == 'pair') and (res2.get('val') == 'pair'):
            if res1['card'] > res2['card']:
                wins +=1 
                continue
            else:
                continue
        else:
            print player1, res1, o1
            print player2, res2, o2
            print ""

    print "wins", wins


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
