#### COPIED ####  VERIFIED
"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters
as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made,
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it
(which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters,
but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""


def min_edit(str):  # No memoization
    if len(str) == 0 or len(str) == 1:  # for a str of len 0 or 1, its already a palindrome
        return 0, str

    if str[0] == str[-1]:  # If both first and last characters are same, consider rest of the str.
        ret_edit, ret_str = min_edit(str[1:len(str)-1])
        ret_str = str[0] + ret_str + str[-1]  # This is the new palindrome to be returned
    else:
        first_edit, first_str = min_edit(str[1:])   # Exclude first character and check
        last_edit, last_str = min_edit(str[:len(str) - 1])  # exlude last character and check

        if first_edit == last_edit:  # If both edit distnaces are same, use lexicographical sorting
            ret_str = str[0] + first_str + str[0] if str[0] < str[-1] else str[-1] + last_str + str[-1]
        else:
            ret_str = str[0] + first_str + str[0] if first_edit < last_edit else str[-1] + last_str + str[-1]
        # One insertion(either first char at end or last character at beginning)
        ret_edit = min(first_edit + 1, last_edit + 1)

    return ret_edit, ret_str


# For memoization, we will use a 2d array of len(str) * len(str). In this,
# i, j will store edit_distance and edited_palindrome for sub-string str[i...j]
def min_edit_memo(str, memo, start, end): # Both start and end inclusive
    if start > end:  # start cannot be > end
        return 0, ''

    if memo[start][end] is not None:  # if memoized, return it
        return memo[start][end]

    if start == end:  # if start == end, it means only one character, which is already a palindrome
        memo[start][end] = (0, str[start])
        return memo[start][end]

    if str[start] == str[end]:
        ret_edit, ret_str = min_edit_memo(str, memo, start+1, end-1)
        ret_str = str[start] + ret_str + str[start]
    else:
        first_edit, first_str = min_edit_memo(str, memo, start+1, end)
        last_edit, last_str = min_edit_memo(str, memo, start, end-1)

        if first_edit == last_edit:
            ret_str = str[start] + first_str + str[start] if str[start] < str[end] else str[end] + last_str + str[end]
        else:
            ret_str = str[start] + first_str + str[start] if first_edit < last_edit else str[end] + last_str + str[end]
        ret_edit = min(first_edit + 1, last_edit + 1)

    memo[start][end] = (ret_edit, ret_str)
    return memo[start][end]


def min_edit_dp(str):
    memo = [[None for i in range(len(str))] for j in range(len(str))]
    min_edit_memo(str, memo, 0, len(str)-1)
    print(memo)
    return memo[0][len(str)-1]


if __name__ == '__main__':
    string = 'abcde'
    print(min_edit(string))
    print(min_edit_dp(string))