### COPIED ###   VERIFIED
from collections import defaultdict

def make_palindrome(string):
    my_hash = defaultdict(int)

    # create a freqency hash table of characters
    for c in string:
        my_hash[c] += 1

    my_list = []  # used to create string
    mid = None
    for character, frequency in my_hash.items():
        if frequency % 2 == 1:
            mid = character  # found a mid character. This may change
            frequency -= 1  # no need of this line as we are doing //2 below

        my_list.extend((character for _ in range(frequency//2)))

    count = len(my_list)
    if mid:
        my_list.append(mid)

    if count:  # dont forget this check. Otherwise, it will duplicate the only element, element '0'
        # for example, if the given string is 'abc', then count will be 0, and due to mid,
        # we will have 'a' or 'b' or 'c' in the list. The below code will duplicate the only character
        # because count - 1 = -1 == last character in the list = my_list[0]
        my_list.extend(my_list[count-1::-1])
    print(''.join(my_list))


make_palindrome('abbaccd')


