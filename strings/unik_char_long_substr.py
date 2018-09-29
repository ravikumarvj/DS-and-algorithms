### COPIED ###

"""
Find the Longest Substring with K Unique Characters
Take string “aabacced” as an example.
If K is 1, the longest substring can be “aa”.
If K is 2, the longest substring can be “aaba”.
If K is 3, the longest substring can be “aabacc”.
"""

def longest_substring(string, k):
    start = 0  # start of sliding window
    end = 0   # end of sliding window

    max_start = 0
    max_largest = 0
    char_dict = {}  # dictionary to hold sliding window's characters

    while end < len(string):
        while end < len(string):  # (re) initialize sliding window
            c = string[end]
            if c in char_dict:
                char_dict[c] += 1
            else:
                if len(char_dict) == k:  # sliding window full
                    break
                char_dict[c] = 1
            end += 1

        # update largest
        if end - start > max_largest:
            max_start = start
            max_largest = end - start

        # decrease the sliding window by 1 character
        while start < end and end < len(string):
            c = string[start]
            char_dict[c] -= 1
            start += 1
            if char_dict[c] == 0:
                del char_dict[c]
                break

    print(string[max_start: max_start + max_largest])


if __name__ == '__main__':
    longest_substring('abccdc', 1)
    longest_substring('aacbaaad', 2)
    longest_substring('aaadbaccaccb', 3)

