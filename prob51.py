#!/usr/bin/python3


'''
    "prob51.py", by Sean Soderman
    Here we're trying to find the first family of 8 prime numbers that all share N digits Y.
    These digits do not have to be contiguous.
'''
from pro51yelpers import genplates
from sieve import makesieve, nextprime

def pf8(): #prime family of size 8
    ONE_MILLION = 10 ** 6
    sieve = makesieve(ONE_MILLION) 
    first = nextprime(56003, sieve) #this is the first prime family of size 7
    theFam = []
    while len(theFam) < 8:
        templates = genplates(first, 8)
        for num in templates.keys():
            temples = templates[num]
            for temple in temples:
                tolerance = 10 - num - 8
                pcpy = first
                nFam = []
                for i in range(num, 10):
                    if sieve[pcpy]:
                        nFam.append(pcpy)
                    else:
                        tolerance -= 1
                    if tolerance < 0:
                        break
                    pcpy += temple
                if tolerance >= 0:
                    break
            if tolerance >= 0:
                theFam = nFam
                break
        first = nextprime(first, sieve)
    print(theFam)

pf8()
