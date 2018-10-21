### COPIED ####  VERIFIED

def print_parentheses(so_far, index, left_count, right_count):
    if left_count == 0 and right_count == 0:
        print(''.join(so_far))
        return

    # if number of left and right are equal, we can put only left parantheses
    if left_count == right_count:
        so_far[index] = '('
        print_parentheses(so_far, index + 1, left_count - 1, right_count)
    else:  # right > left. Try both left and right. (There is no left > right)
        if left_count:
            so_far[index] = '('
            print_parentheses(so_far, index + 1, left_count - 1, right_count)
        so_far[index] = ')'
        print_parentheses(so_far, index + 1, left_count, right_count - 1)
    return

def generate_parenthesis(count):
    if count%2:
        return None
    half = count//2

    p_list = [0]* count

    # keep a left count and right count to keep track of left and right parenthesis
    print_parentheses(p_list, 0, half, half)

generate_parenthesis(6)


def print_numbers(p_list, index, one_half, zero_half):
    if index == len(p_list):
        print(''.join(p_list))
        return

    p_list[index] = '1'
    print_numbers(p_list, index + 1, one_half + 1, zero_half)

    if one_half != zero_half:
        p_list[index] = '0'
        print_numbers(p_list, index + 1, one_half, zero_half + 1)


def generate_numbers(count):
    one_half = count // 2 + count % 1
    zero_half = count // 2

    p_list = [0] * count
    p_list[0] = '1'

    print_numbers(p_list, 1, 1, 0)

generate_numbers(5)