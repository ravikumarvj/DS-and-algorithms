### COPIED ###


# Solved using sliding window, as well as keeping count of each character of array within the sliding window
# array should have only unique characters
def find_min_substr(string, array):
    s = dict()
    for i in array:  # Move the elements of array to a dictionary,
        s[i] = 0     # for easy lookup as well as for keeping count

    start, end = 0, 0  # Sliding window (SW)
    total = 0          # Number of elements of array, currently withing SW
    min_len, min_start = len(string) + 1, 0   # minimum length we have seen so far

    while end < len(string):
        while end < len(string):  # increase window such that all the elements
            c = string[end]       # of array is within window.
            end += 1              # This may include redundant characters in the
            if c not in s:        # front of the window
                continue

            if s[c] >= 1:         # If a member of array is already seen increase its count
                s[c] += 1
            else:
                s[c] = 1
                total += 1
                if total == len(s):  # Once all the elements are found, close the window
                    break

        # Either total == len(set) or end == len(string)
        while start < len(string):  # remove leading redundant characters
            c = string[start]
            start += 1
            if c not in s:
                continue
            if s[c] > 1:
                s[c] -= 1
            else:  # move as much, such that total is about to be decreased.
                length = end - start + 1  # New length
                if length < min_len:
                    min_len = length
                    min_start = start - 1

                s[c] -= 1  # s[c] is now 0. So, decrease total
                total -= 1  # break out of loop now.
                break

    # String parsing over
    if min_len < len(string):
        print(min_start, min_len)
        print(string[min_start:min_start + min_len])
    else:
        print('None')


from collections import defaultdict


def minWindow(s, t):
    hasht = defaultdict(int)
    # Create hash for storing crctrs and their frq of word t.
    total_c = 0
    for c in t:
        hasht[c] += 1

    # total number of unique chars in t
    total_c = len(hasht)

    # For storing details of min window found so far.
    min_start, min_end, min_len = 0, 0, len(s) + 1
    # current window
    start, end = 0, 0

    while end < len(s):
        # Fill the window
        while end < len(s):
            c = s[end]
            # Always think about loop variables: NBNBNBNB
            end += 1  # keep this here, because it needs to be done before break.
            if c in hasht:
                hasht[c] -= 1  # hasht[c] could go negative
                if hasht[c] == 0:  # c satisfied
                    total_c -= 1  # this character is done
                    if total_c == 0:  # all chars done
                        break  # window full

        # optimize the window.
        while total_c == 0 and start < end:
            c = s[start]
            if c not in hasht:
                start += 1
                continue
            # perfect window
            if hasht[c] == 0:  # adding one to it, will break the window
                if end - start < min_len:
                    min_start = start
                    min_end = end
                    min_len = min_end - min_start
                break

            # c can be optimized
            hasht[c] += 1  # c was negative
            start += 1  # Always think about loop variables

        # break window
        hasht[s[start]] += 1
        total_c += 1  # Dont forget to increase total_c,  when breaking window
        start += 1

    if min_len < len(s):
        print(s[min_start:min_end])
        return s[min_start:min_end]

    return ''



if __name__ == '__main__':
    # string = 'xaxzbyxaabyyzcxbbyyzxx'
    string = 'xyzdaaabcdabcad'
    array = ['a', 'b', 'd']
    find_min_substr(string, array)
    string = 'xyzdaaabcdabcad'
    t = 'abd'
    minWindow(string, t)