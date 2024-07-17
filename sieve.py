#!/usr/bin/env python3

'''
    Really simple implementation of a prime sieve. No skiplist for nextprime
    currently, either.
'''
from math import sqrt

def makesieve(ceiling):
    s = [True] * ceiling
    s[0] = False
    s[1] = False
    for i in range(2, int(sqrt(ceiling)) + 1):
        if s[i] is not False:
            starter = i+i
            while starter < ceiling:
                s[starter] = False
                starter += i
    return s

def pprint(s):
    for i in range(0, len(s)):
        if s[i] is True:
            print(i)

def nextprime(n, sieve):
    n += 1
    while not sieve[n]:
        n += 1
    return n
