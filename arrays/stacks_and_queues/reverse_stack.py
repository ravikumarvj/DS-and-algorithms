### COPIED ### VERIFIED
"""
Reverse a stack using recursion

Write a program to reverse a stack using recursion. You are not allowed to use loop constructs like while, for..etc, and you can only use the following ADT functions on Stack S:
isEmpty(S)
push(S)
pop(S)
"""
"""
sort a stack using recursion. Top element should be the smallest
"""

from queue import LifoQueue


# Given a stack with push(), pop(), empty() operations,
# delete middle of it without using any additional data structure.
def _delete_middle(stack, count):  # COPIED
    if stack.empty():
        # when stack is empty, the count will have the number of elements.
        # middle is half of that. return middle
        middle = (count // 2) + 1  #5//2 + 1 = 3. Count starts from 1. not 0
        # print(count, middle)
        return middle
    top = stack.get()
    count += 1
    middle = _delete_middle(stack, count)

    # if count == 4, mid = 3. So, 3rd element from top will be deleted.
    # If we want otherwise, make middle = (count + 1)//2 rather than (count//2) + 1
    if middle != count:  # Found half
        stack.put(top)
    return middle

def delete_middle_stack(stack):  # COPIED
    count = 0
    _delete_middle(stack, count)


def insert_bottom(stack, top):  ## COPIED
    if stack.empty():
        stack.put(top)
        return
    # remove the top
    new = stack.get()
    insert_bottom(stack, top)
    # add back the top
    stack.put(new)


def reverse_stack(stack):  ## COPIED
    if stack.empty():
        return

    # Get the top element
    top = stack.get()

    # Recursively reverse
    reverse_stack(stack)

    # Insert the top at the bottom
    insert_bottom(stack, top)


def insert_position(stack, element):  # COPIED
    if stack.empty():
        stack.put(element)
        return
    top = stack.get()
    if element > top:
        insert_position(stack, element)
        stack.put(top)
    else:
        stack.put(top)
        stack.put(element)


def stack_sort(stack):  # COPIED
    if stack.empty():
        return

    # Get the top element
    top = stack.get()
    # recursively sort the stack
    stack_sort(stack)

    # insert the element at the position
    insert_position(stack, top)

if __name__ == '__main__':
    stk = LifoQueue()

    for i in range(18):
        stk.put(i)


    # reverse_stack(stk)
    delete_middle_stack(stk)

    # stack_sort(stk)
    #print('-' * 10)
    while not stk.empty():
       print(stk.get())