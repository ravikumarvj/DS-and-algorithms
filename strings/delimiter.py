### COPIED ###  VERIFIED

"""
Write an algorithm to determine if all of the delimiters in an expression are matched and closed.
For example, “{ac[bb]}”, “[dklf(df(kl))d]{}” and “{[[[]]]}” are matched. But “{3234[fd” and {df][d} are not.
"""
from queue import LifoQueue

is_opening = {'{', '[', '('}  # set and dictionary for O(1) lookup
close_d = {'}':'{', ']':'[', ')':'('}

def delimiter_match(string):
    stk = LifoQueue()

    for c in string:
        if c in is_opening:
            stk.put(c)
        elif c in close_d:
            if stk.empty():
                return False
            s = stk.get()
            if s != close_d[c]:
                return False

    if stk.empty():
        return True
    return False


if __name__ == '__main__':
    print(delimiter_match('{[[[]]]}{3234[fd]}{df[]d}()'))
    print(delimiter_match('[dklf(df(kl))d]{}'))
    print(delimiter_match('{a[v[b[n(mk]r)e]r]t]y}o'))
    print(delimiter_match('{{3234[f]d}'))