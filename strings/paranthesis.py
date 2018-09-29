### COPIED ###
"""
"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds
the corresponding closing parenthesis. Example: if the example string above is input with the
number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).
"""


from queue import LifoQueue


def find_closing(string, start):  # start is 0 based index
    if len(string) + 2 < start:
        return

    if string[start] != '(':
        print(None)
        return

    count = 1

    for i in range(start + 1, len(string)):
        if string[i] == ')':
            count -= 1
            if count == 0:
                print(i)
                return
        elif string[i] == '(':
            count += 1

    print('None')


if __name__ == '__main__':
    string = "()"
    find_closing(string, 0)