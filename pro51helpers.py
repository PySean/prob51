#!/usr/bin/env python3
'''
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
