### COPIED ###  VERIFIED

"""
Longest Substring without Repeating Characters

Given a string, find the longest substring without repeating characters.
For example, for string “abccdefgh”, the longest substring is “cdefgh”.

"""

def long_substring(string):
    win_start = 0
    win_end = 0
    max_start = 0
    max_length = 0
    s = set()  # no need of dictionary

    while win_end < len(string):  # think about when the len ends...
        c = string[win_end]
        if c not in s:  # if c not there, add it.
            s.add(c)
            win_end += 1
            if win_end - win_start > max_length:  # update max length
                max_length = win_end - win_start
                max_start = win_start
        else:
            # remove a character from start and continue till string[win_end] is removed from set
            # could have written a loop here, but this is more consice
            c = string[win_start]
            s.remove(c)
            win_start += 1

    print(string[max_start: max_start + max_length])


if __name__ == '__main__':
    long_substring('abccdefghh')
