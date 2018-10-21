### COPIED ###  VERIFIED
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
    array = ['a', 'b', 'd', 'd']
    find_min_substr(string, array)
    string = 'xyzdaaabcdabcad'
    t = 'abdd'
    minWindow(string, t)