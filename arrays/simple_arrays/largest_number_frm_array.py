### COPIED ###
from functools import cmp_to_key

def my_cmp(a, b):  # Normal comparator. -1 if a < b, 0 if a==b and 1 if a>b.
    one = str(a) + str(b)
    two = str(b) + str(a)
    if one < two:
        return -1
    if one == two:
        return 0
    return 1

# [].sort() have key. But it takes only a single argument. Same is the case with sorted()
# to convert key to a comparator function taking two arguments, use functools.cmp_to_key
def make_largest(array):
    # Can avoid reverse by changing cmp() function to return 1, 0, -1 instead of -1, 0, 1
    array.sort(key=cmp_to_key(my_cmp), reverse=True)  # in place sort
    print(''.join([str(a) for a in array]))


# array = [72, 70, 7, 9, 76, 78, 5]
# array = [1, 34, 3, 98, 9, 76, 45, 4]
# make_largest(array)


from functools import cmp_to_key

def my_cmp(a, b): # Normal comparator. -1 if a < b, 0 if a==b and 1 if a>b.
    one = str(a) + str(b)
    two = str(b) + str(a)
    if one < two:
        return -1
    if one == two:
        return 0
    return 1

array = [72, 70, 7, 9, 76, 78, 5]
print(sorted(array, key=cmp_to_key(my_cmp)))
