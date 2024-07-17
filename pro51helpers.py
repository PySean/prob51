#!/usr/bin/env python3
'''
    Some definitions are in order. This problem wants us to find a "family" of primes of
    size 8. It defines a "family" thusly: a set of prime numbers that each differ in exactly n
    digits, and each of those shared digits is equal to another. An example of a nonprime
    family would be 191, 292, 393, 494. This family is of size 4, they only differ 
    in the first and last digits, and those digits match. A "template" can be used to 
    achieve this result. I define a template as a number comprised wholly of 0 and 1. 

    Here, we could use the template 101, and, starting with 191, can "progress" 191
    to 292, 393, and 494 with repeated additions. Now, it is worth mentioning
    that it isn't necessarily the case that we wish to progress each matching number
    simultaneously. Which is why I generate all possible templates for a given set
    of matching digits within a given number, which is precisely what this following
    code does. The size of the family does thankfully restrict us. Based on the size,
    we limit the digits we look at, because for example, for a family of size 8, 
    we would only be able to generate a family of at most size 5 if we begun with 5.

    For all matching digits that meet our family size requirements,
    generate all possible templates for those digits, and do it for all such digits
    present within the number.
'''
def genplates(num, famSz) -> {int: int}:
    #Create the array composed of the numbers from "num", where each number that isn't
    #a candidate for progression is replaced with a sentinel value of -1.
    progressions = [d if d <= 10 - famSz else -1 for d in map(int,str(num))]
    nums = set(filter(lambda x: x != -1, progressions))
    dictProgs = {}
    for i in nums:
        occs_of_i = [x if x == i else -1 for x in progressions]
        dictProgs[i] = tempgen(occs_of_i)
    return dictProgs

def tempgen(ll, num=0):
    if len(ll) == 0:
        if num == 0:
            return []
        return [num]
    temps = []
    if ll[0] > -1:
        slat = 10 ** (len(ll) - 1)
        temps += tempgen(ll[1:], slat + num)

    temps += tempgen(ll[1:], num)
    return temps
