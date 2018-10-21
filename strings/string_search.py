#### COPIED #### VERIFIED
from collections import defaultdict

def find_pattern(pattern, string):  # find pattern in string  # COPIED
    for s in range(len(string) - len(pattern) + 1):  # No need to loop completely
        p = 0
        while pattern[p] == string[s + p]:  # Note s + p. S is not changed in this loop
            p += 1
            if p == len(pattern):
                print('pattern found at:', s, ' ', string[s: s + len(pattern)])
                break

    return None


# Compute hash
def my_hash (string):  # COPIED
    prime = 101
    base = 256
    hash_val = 0

    for i in string:
        hash_val = ((hash_val * base) + ord(i)) % prime  # ord()

    return hash_val


# Re-compute hash
def find_my_hash(old_hash, string, exclude_i, include_i):  # COPIED
    prime = 101
    base = 256

    decr = ord(string[exclude_i])
    length = include_i - exclude_i - 1  # decr wil have ord(x) * 256^(len - 1)

    while length:
        decr = (decr * base) % prime  # avoid overflow by doing % 101 each time
        length -= 1

    old_hash = (old_hash + prime - decr) % prime  # decrease the exclude. (prime is added to avoid -ve)

    return ((old_hash * base) + ord(string[include_i])) % prime


def find_multiple_pattern(patterns, string):  # Rabin-karp Algorithm  # COPIED
    # patterns is a set of patterns
    pat_dict = defaultdict(list)
    len_set = set()

    # create a dictionary of hash->pattern. for accommodating hash collisions, use list
    for pat in patterns:
        pat_dict[my_hash(pat)].append(pat)
        len_set.add(len(pat)) # If all pattern is of same length, this is not needed

    len_list = list()

    # allow for multiple length patterns
    for length in len_set:
        s_hash = my_hash(string[:length])
        # list contains length, current hash value.
        # Note that for a length, we need to only store a single hash value
        len_list.append([length, s_hash])  # dont use tuple (length, s_hash). It is not modifiable

        if s_hash in pat_dict:
            # use 'in' as pat_dict[s_hash] is a list
            if string[:length] in pat_dict[s_hash]:  # not perfect hash. so this check is mandatory
                print('pattern: ', string[:length], 'found at 0')

    for i in range(len(string)):
        for ll in range(len(len_list)):
            length, s_hash = len_list[ll]
            if i < length:
                continue
            new_hash = find_my_hash(s_hash, string, i - length, i)
            if new_hash in pat_dict:
                if string[i-length + 1 : i + 1] in pat_dict[new_hash]:
                    print('pattern: ', string[i-length + 1 : i + 1], 'found at ', i - length + 1)
            len_list[ll][1] = new_hash

    return None


def pre_process_pattern(pattern):  # COPIED
    lps = [0] * len(pattern)
    length = 0  # length of a matching prefix seen so far
    i = 1

    # This is like dynamic programming
    while i < len(pattern):
        # if last character if sub-pattern matches last character of longest prefix matched yet
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length == 0: # No previous matches
                lps[i] = 0  # No matching prefix
                i += 1
            else: # go back and check previous prefixes
                length = lps[length - 1]  # decrease 1 from prevoius longest prefix match
                # Dont increase i here

    print(lps)
    return lps


def find_pattern_kmp(pattern, string):  # COPIED
    if len(string) < len(pattern):
        return None

    lps = pre_process_pattern(pattern)

    i, j = 0, 0 # i goes over string and j over pattern
    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                print('Found match at', i-len(pattern))
                j = lps[j-1]  # dont reset j to 0
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]  # j-1 match of prefix

    return



pattern = 'abababb'
string = 'abababbabababababbabb'

# find_pattern(pattern, string)

# pat_list = ['aa', 'axb', 'axde', 'aaxd']  # aa and axde have same hash value
# find_multiple_pattern(pat_list, 'aaxaabaxdbaaaxbaaxde')

find_pattern_kmp(pattern, string)