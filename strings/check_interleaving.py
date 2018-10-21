### COPIED ###  VERIFIED

def check_interleaving_r(main, sub_1, sub_2, main_index, sub_1_index, sub_2_index):
    if main_index == len(main) and sub_1_index == len(sub_1) and sub_2_index == len(sub_2):
        return True

    if main_index == len(main):  # in any other case, return false if main is done.
        return False

    if sub_1_index < len(sub_1) and main[main_index] == sub_1[sub_1_index]:
        if check_interleaving_r(main, sub_1, sub_2, main_index + 1, sub_1_index + 1, sub_2_index):
            return True

    if sub_2_index < len(sub_2) and main[main_index] == sub_2[sub_2_index]:
        if check_interleaving_r(main, sub_1, sub_2, main_index + 1, sub_1_index, sub_2_index + 1):
            return True

    return False


def check_interleaving(main, sub_1, sub_2):
    return check_interleaving_r(main, sub_1, sub_2, 0, 0, 0)


main = 'ACBABC'
sub_1 = 'ACB'
sub_2 = 'CBA'

print(check_interleaving(main, sub_1, sub_2))
