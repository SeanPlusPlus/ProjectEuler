#!/usr/bin/env python

import itertools
import operator


def getCipherText():
    f = open('p059_cipher.txt')
    lines = f.readlines()[0]
    li = []
    for l in lines.split(','):
        li.append(int(l.strip('\n')))
    return li


def main():
    the = [116, 104, 101]  # ascii vals for "the"

    # list of all possible xor'd triples for "the" from lowercase letters
    the_triples = []
    for j in range(97, 123):
        for k in range(97, 123):
            for l in range(97, 123):
                the_triples.append([the[0] ^ j, the[1] ^ k, the[2] ^ l])

    # all three character triples in our cipher text
    cipher_triples = []
    cipher = getCipherText()
    for i, c in enumerate(cipher):
        try:
            li = [cipher[i], cipher[i+1], cipher[i+2]]
            cipher_triples.append(li)
        except IndexError:
            pass

    # search cipher for instances of any the_triples occuring
    di = {}
    for t in the_triples:
        for c in cipher_triples:
            if t == c:
                if str(c) in di:
                    di[str(c)] += 1
                else:
                    di[str(c)] = 1

    sorted_di = sorted(di.items(), key=operator.itemgetter(1))

    # the two most frequent triples above are: [16, 15, 10] and [19, 7, 1]

    # for idx, el in enumerate([16, 15, 10]):
    #     print chr(the[idx] ^ el), (the[idx] ^ el)

    # the above produces g d o

    # for idx, el in enumerate([19, 7, 1]):
    #     print chr(the[idx] ^ el), (the[idx] ^ el)

    # the above produces g o d
    # let's assume that is the key and decrupt the cipher text vals

    god = [103, 111, 100]
    decrypted = []
    for i, el in enumerate(cipher):
        decrypted.append(el ^ god[i % 3])

    message = ""
    for el in decrypted:
        message += chr(el)

    print message
    print "answer:", sum(decrypted)

if __name__ == '__main__':
    main()
