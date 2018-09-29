



def find_palindrome(string, i, j):  # COPIED
    while i >= 0 and j < len(string) and string[i] == string[j]:
        i -= 1
        j += 1
    return string[i+1:j] # string[i] != string[j] exclude them. Or i = -1 or j = len(string)

def longest_palindromic_substring(string):  # COPIED
    if len(string) <= 0:
        return ''
    longest = string[0] # useful for string with single character

    for i in range(1, len(string)):
        temp1 = find_palindrome(string, i-1, i)  # even length, center i-1 and i
        temp2 = find_palindrome(string, i-1, i+1) # odd length, center i
        if len(temp1) > len(longest) or len(temp2) > len(longest):
            longest = temp1 if len(temp1) > len(temp2) else temp2

    return longest

def check_rotated_palindrome(string):
    temp = string + string  # Patterns for anything circular
    s = set()
    for i in string:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    odd = None
    if len(s) > 1:
        return False
    if len(s) == 1:
        odd = s.pop()

    N = len(string)

    if odd:
        for i in range(2*N):
            if temp[i] == odd:
                break
        window = temp[i-(N//2):i+(N//2)+1]
        ret = check_palindrome(window)
        return ret, window
    else:
        for i in range(N//2, 2*N - (N//2)):
            if temp[i] == temp[i-1]:
                window = temp[i-(N//2):i+(N//2)]
                ret = check_palindrome(window)
                if ret:
                    return ret, window


def check_palindrome(string):   # COPIED
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def check_any_anagram_palindrome(string):   # COPIED
    st = set()
    for c in string:
        if c in st:
            st.remove(c)
        else:
            st.add(c)
    if len(st) > 1:
        return False
    return True

if __name__ == '__main__':
    # print(check_palindrome('amalayxyalama'))
    # print(check_any_anagram_palindrome('aacxxyciix'))
    # print(check_rotated_palindrome('malyalam'))
    print(longest_palindromic_substring('layalammalayalamma'))

    print(isomorphic_strings('abbcb', 'zxxyz'))