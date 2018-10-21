### COPIED ###  VERIFIED
"""
Given two strings, determine if they are isomorphic.
Two strings X and Y are called isomorphic strings if all occurrences of each character in X can be
replaced with another character to get Y and vice-versa.
For eg, consider the strings ACAB, XCXY. They are isomorphic
"""
def isomorphic_strings(s1, s2):  # Symmetric relation
    forward = dict()
    reverse = set()

    # S1 and S2 shoulg be of equal length, as this is symmetric relation
    if len(s1) != len(s2):
        return False

    for i, j in zip(s1, s2):
        # already seen?
        if i in forward and forward[i] != j:
            return False
            # reverse.
        elif i not in forward:
            if j in reverse: # j in reverse, though i not in forward
                return False
        forward[i] = j
        reverse.add(j)

    return True

print(isomorphic_strings('abaca', 'xyxyx'))
print(isomorphic_strings('abaca', 'xyxzx'))
print(isomorphic_strings('abaa', 'abaa'))
print(isomorphic_strings('abaa', 'babb'))
print(isomorphic_strings('aa', 'xy'))