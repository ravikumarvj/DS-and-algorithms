### COPIED ####  VERIFIED
"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# Note set cannot contain another set as set is modifiable. So we will create a set of tuples
"""

def generate_power_set(in_set):
    if len(in_set) == 0:
        return set()

    ret1 = set()
    ret1.add(())
    ret2 = set()
    # l = tuple(in_set)

    for num in in_set:
        for res in ret1:
            ret2.add(res)  # Copy already existing elements and make another copy
            ret2.add(res + (num, )) # with num added to all those existing
        ret1 = ret2  # make ret1 point to ret2 and ret2 to empty set
        ret2 = set()

    print(ret1)

from math import log2
from math import pow

def genetarte_power_set_2(in_set):
    n = len(in_set)
    l = tuple(in_set)  # make tuple to have fixed ordering

    ret = set()

    for i in range(int(pow(2, n))):  # loop until 2^n. For example, if n = 3, go from 0-7
        num = i
        result = []
        while num: # For whichever bit is set in num, add corresponding elements to result
            bit_set = int(log2(num ^ (num & (num - 1))))
            result.append(l[bit_set])
            num &= (num - 1)
        ret.add(tuple(result))

    print(ret)

if __name__ == '__main__':
    generate_power_set({'a', 'b', 'a'})
    genetarte_power_set_2({'a', 'b', 'a'})