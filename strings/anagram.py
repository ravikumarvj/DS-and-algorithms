#### COPIED #### VERIFIED
"""
Problem 1: Given two strings, check if the strings are anagrams of each other
Problem 2: Given two strings, string1 and string2, check if string1 contains an anagram of string2
"""

from collections import defaultdict


# O(N) runtime, O(N) space
def check_anagrams_hash (str1, str2):   ### COPIED
    alphs = defaultdict(int)

    for c in str1:
        alphs[c] += 1

    for c in str2:
        alphs[c] -= 1
        if alphs[c] == 0:
            del alphs[c]

    if len(alphs):
        print(str1, 'and', str2, 'are not anagrams')
    else:
        print(str1, "is an anagram of", str2)


# O(N) runtime, O(N) space, if immutable DS is used. For mutable string O(1), if input is allowed to be modified
def check_anagrams_sort(str1, str2):  # Copied
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)  # strings in python are immutable. So needs O(N) space
    str2 = sorted(str2)  # string don't have sort method as in str1.sort()

    for i, j in zip(str1, str2):
        if i != j:
            return False

    return True


# O(m) runtime, O(n) space. m = len(str1), n = len(str2) and m > n
def contains_anagram_hash(str1, str2):  # Copied
    alphs = defaultdict(int)

    for c in str2:
        alphs[c] += 1

    for c in str1:
        if c in alphs:
            alphs[c] -= 1
            if alphs[c] == 0:
                del alphs[c]

    if len(alphs):
        print(str1, 'does not contain', str2, "'s anagrams")
    else:
        print(str1, "contains an anagram of", str2)


# O(mlogm) runtime, where m is the len(str1). O(m) space for sorting, if immutable str.
def contains_anagram_sort(str1, str2):  # COPIED
    if len(str1) < len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    i, j = 0, 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            j += 1
            i += 1
        else:
            i += 1

    if j == len(str2):
        return True

    return False


def contains_anagram_conseq (str1, word):  # find word in str1  # COPIED
    if word == '' or len(str1) < len(word):
        print(str1, 'does not contain', word, "'s anagrams")
        return

    alphs = defaultdict(int)  # defaultdict as hash table
    # Add characters of word in to hash table
    for c in word:
        alphs[c] += 1

    # From str1, update alphs hash upto sliding window size (len(word))
    for i in range(len(word)):
        c = str1[i]
        # existing character's count will decrease. New character will start as negative number
        # for example, if word = ab and str1 = axba, before this, alphs will have a=1, b=1
        # after this, alphs will have b=1 and x=-1
        alphs[c] -= 1
        if alphs[c] == 0:
            del alphs[c]

    start = 0
    end = len(word)
    # move the sliding window to the end of str1. Check if hash table is empty at each move
    while len(alphs) and end < len(str1):
        c = str1[end]
        alphs[c] -= 1
        if alphs[c] == 0:
            del alphs[c]

        e = str1[start]  # Always do like this to avoid confusions
        alphs[e] += 1    # alphs is defaultdict
        if alphs[e] == 0:  # anything that was negative before might get deleted here
            del alphs[e]

        start += 1
        end += 1

    # Check again to be sure. May be loop exited when end of str1 is reached
    if len(alphs) == 0:
        print(str1, "contains an anagram of", word)
        print(str1[start:end])
    else:
        print('NOOOO')


"""
Given a word and a string S, find all starting indices in S which are anagrams of word.
For example, given that word is “ab”, and S is “abxaba”, return 0, 3, and 4.
"""

def print_all_anagram_starts(word, string):  # COPIED
    hash = defaultdict(int)
    ret = []

    # initialize hash with word
    for c in word:
        hash[c] += 1

    # Change the hash with initial len(word) characters from string
    for i in range(len(word)):
        c = string[i]
        hash[c] -= 1
        if hash[c] == 0:
            del hash[c]

    # check if word's anagram is found
    if len(hash) == 0:
        ret.append(0)

    start = 0
    for i in range(len(word), len(string)):
        c = string[i] # include c
        hash[c] -= 1
        if hash[c] == 0:
            del hash[c]

        e = string[start]  # exclude e
        hash[e] += 1
        if hash[e] == 0:
            del hash[e]
        start += 1  # increment start here. 'i' is incremented automatically

        if len(hash) == 0:  # Found a match
            ret.append(start)

    print(ret)
    return ret


def group_anagram_hash(arr):  # COPIED
    # sorted on a word will return a list.
    aux_arr = [''.join(sorted(word)) for word in arr]  # Dont forget ''.join
    hash = defaultdict(list)

    # you can avoid aux_array and do the sorting here, if needed.
    for i in range(len(aux_arr)):
        hash[aux_arr[i]].append(i)

    for word_list in hash.values():
        for index in word_list:
            print(arr[index], end=' ')

        print('')
    return


def group_anagram_sort(arr):  # COPIED
    # sorted on a word will return a list. For each sorted word, keep word as backup (or keep index to arr)
    aux_arr = [(''.join(sorted(word)), word) for word in arr]  # Dont forget ''.join
    aux_arr.sort(key=lambda x:x[0])  # key=; not cmp=

    i = 0
    while i < len(aux_arr)-1:
        if aux_arr[i][0] == aux_arr[i+1][0]:
            print(aux_arr[i][1], end=' ')
        else:
            print(aux_arr[i][1])
        i+=1
    print(aux_arr[-1][1])
    return



if __name__ == '__main__':
    # check_anagrams_hash('lalanagrkamaskkk', 'lskgarkaalmkanka')
    # print(check_anagrams_sort('lalanagrkamaskkk', 'lskgarkaalmkanka'))

    # contains_anagram_hash('lskfhlarlmoasskkkkp', 'ksrloalap')
    # print(contains_anagram_sort('lskfhlarlmoasskkkkp', 'ksrloalpa'))
    word = 'ab'
    string = 'aaaxbbabcaaacb'

    # contains_anagram_conseq(string, word)
    word = 'word'
    string = 'swordandwordrownoutwords'
    print_all_anagram_starts(word, string)

    arr = ['actors','costar','altered','related','auctioned','education','aspired','despair','mastering','streaming','recursed','secured']
    # arr = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
    group_anagram_hash(arr)
    print('----')
    group_anagram_sort(arr)