
def pattern_match_rec(string, s_in, pattern, p_in, match):
    if p_in == len(pattern) and s_in == len(string):
        return True

    if p_in == len(pattern) or s_in == len(string):
        return False

    next_pat = pattern[p_in]
    if next_pat in match:
        string_chars = match[next_pat]
        if len(string) - s_in < len(string_chars):
            return False
        if string_chars != string[s_in:s_in + len(string_chars)]: ### 's_in +'
            return False
        return pattern_match_rec(string, s_in + len(string_chars), pattern, p_in + 1, match)

    for i in range(s_in, len(string)):
        string_chars = string[s_in:i+1]
        match[next_pat] = string_chars
        if pattern_match_rec(string, s_in + len(string_chars), pattern, p_in + 1, match):
            return True
        del match[next_pat]

    return False


def pattern_match(string, pattern):
    match = {}
    ret = pattern_match_rec(string, 0, pattern, 0, match)
    print(match)
    return ret


string = 'codecodecode'
pattern = 'xyx'
print(pattern_match(string, pattern))
