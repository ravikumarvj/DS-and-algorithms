from queue import LifoQueue

class Node:  ## COPIED
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Sll:
    def __init__(self): # If you include a tail as well, we can simplyfy a lot of operations
        self.head = None  ## COPIED

    def insert_end(self, data):  ### COPIED
        node = Node(data)
        if self.head is None:  # Head is none handled as special case
            self.head = node
            return

        temp = self.head
        while temp.next:  # No need to save previous
            temp = temp.next

        temp.next = node

    def insert_beg(self, data):  ## COPIED
        self.head = Node(data, self.head)

    def insert_ascend(self, data):  # COPIED
        node = Node(data)
        if self.head is None or self.head.data >= data:
            node.next = self.head
            self.head = node
            return

        temp = self.head.next
        prev = self.head
        while temp:
            if temp.data > data:
                break
            prev = temp
            temp = temp.next

        node.next = prev.next
        prev.next = node

    def remove(self, data):  # COPIED
        if self.head is None:
            return

        temp = self.head
        prev = None

        while temp:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp:
            if prev is None:  # Removing head
                self.head = temp.next
            else:
                prev.next = temp.next

    def _merge(self, first, second):  # Copied
        if first.data < second.data:
            start = first
            first = first.next
        else:
            start = second
            second = second.next

        curr = start
        while first and second:
            if first.data < second.data:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next

            curr = curr.next

        if first:
            curr.next = first
        else:
            curr.next = second

        return start

    def _merge_sort(self, start):  # COPIED
        if start is None or start.next is None:
            return start  # Dont forger to return start
        slow = start
        fast = start

        # Find middle of LL
        while fast.next:
            fast = fast.next.next
            if fast is None:
                break
            slow = slow.next

        save = slow.next
        slow.next = None  # break linked list in to two halves
        start = self._merge_sort(start)  # Dont forger to update the ret val
        save = self._merge_sort(save) # Dont forger to update the ret val

        return self._merge(start, save)

    def merge_sort(self):  # COPIED
        # NB: update the head
        self.head = self._merge_sort(self.head)

    def clone(self):  ## COPIED
        sll = Sll()

        if self.head is None:
            return sll

        sll.head = Node(self.head.data, self.head.next)  # Dont forget
        temp_self = self.head.next
        temp_sll = sll.head  # Used as previous

        while temp_self:
            temp_sll.next = Node(temp_self.data, temp_self.next)
            temp_sll = temp_sll.next
            temp_self = temp_self.next

        return sll

    def reverse(self):  # COPIED
        if self.head is None or self.head.next is None:
            return

        a = self.head
        b = a.next
        c = b.next
        a.next = None  # a will be the last node, after reversal

        while c:
            b.next = a
            a, b, c = b, c, c.next

        b.next = a
        self.head = b

    def pop(self):  # COPIED
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def remove_duplicate_in_sorted(self):  # COPIED
        tmp = self.head
        while tmp.next:
            if tmp.data == tmp.next.data:
                tmp.next = tmp.next.next
                # No need to update tmp, as there could be more than one of each item
            else:
                tmp = tmp.next

    def find_middle_element(self):  # COPIED
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def move_even_nodes_end_reverse(self):  # COPIED
        # An easier solution will be to use stack for alternate nodes
        if self.head is None or self.head.next is None:
            return

        temp = self.head
        new_head = None  # Create a new head for alternate nodes

        while temp and temp.next:
            save = temp.next # Save the even node
            temp.next = temp.next.next
            if temp.next:  # Do this so that we always get the last node
                temp = temp.next

            save.next = new_head  # insert the even node to new head
            new_head = save

        temp.next = new_head  # Put the new list at the end

    def kth_node_from_last(self, k):  # COPIED
        # kth node from last is n-k+1 node from beginning
        # So, if k = 1, we should return last node.
        # K's valid range is 1-n
        if k < 1 or self.head is None:
            return None

        jump = self.head
        while k:
            jump = jump.next
            k -= 1
            if k and jump is None:
                return None

        start = self.head

        while jump:
            jump = jump.next
            start = start.next

        return start.data

    def move_last_to_front(self):  # COPIED
        if self.head is None or self.head.next is None:
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next

        save = temp.next  # last node
        temp.next = None  # end list at previous

        save.next = self.head
        self.head = save

    # Can be done easily if the node is not the last node.
    def delete_node_given_node(self, node):  # COPIED
        if self.head is node:
            self.head = node.next
            return
        if node.next:
            # Replace next node with this node and delete this node
            node.data = node.next.data
            node.next = node.next.next
        else:
            # it is the last node. Traverse and delete
            temp = self.head
            while temp.next is not node:
                temp = temp.next
            temp.next = None

    def rotate(self, k):  # Rotate by k. 0 < K < N
        if self.head is None or self.head.next is None:
            return

        if k <= 0: return
        # If we do 1 rotation, its making last Node as head
        # 2 rotaton ==> 2nd node from last as head
        # K rotation ==> kth node from last as head
        # If K can be > N, we need to first calculate length and then do K % N
        ktemp = self.head
        while k > 0:
            if ktemp is None:
                return # K > N
            ktemp = ktemp.next
            k -= 1

        temp = self.head
        prev = None
        last_node = None
        while ktemp:
            last_node = ktemp  # Needed to create loop
            ktemp = ktemp.next
            prev = temp
            temp = temp.next

        if prev is None: # k == N
            return

        last_node.next = self.head  # Create loop
        prev.next = None        # break loop
        self.head = temp        # New head

    def arrange_alternate_highs(self):  # COPIED
        if self.head is None or self.head.next is None:
            return

        prev = self.head  # Keep a previous node
        temp = self.head.next   # start from second node
        while temp:
            if prev.data > temp.data:
                prev.data, temp.data = temp.data, prev.data
            prev = prev.next.next

            if temp.next:
                if temp.data < temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next.next
            else:
                temp = temp.next

    def __str__(self):  # COPIED
        temp = self.head
        ret = 'Head'
        while temp:
            ret += ' -> ' + str(temp)
            temp = temp.next

        return ret


def sll_merge(s1, p2):   # COPIED
    # Merge and return a new sll. remove s1 and p2
    sll = Sll()
    if p2 is None:
        sll.head = s1.head
        s1.head = None
        return
    if s1 is None:
        sll.head = p2.head
        p2.head = None
        return

    stemp = s1.head
    ptemp = p2.head

    if ptemp.data < stemp.data:
        sll.head = ptemp
        ptemp = ptemp.next
    else:
        sll.head = stemp
        stemp = stemp.next
    curr = sll.head

    while stemp and ptemp:
        if ptemp.data < stemp.data:
            curr.next = ptemp
            ptemp = ptemp.next
        else:
            curr.next = stemp
            stemp = stemp.next
        curr = curr.next  # Dont forget this

    if ptemp:
        curr.next = ptemp
    else:
        curr.next = stemp
    s1.head = None
    p2.head = None

    return sll

def merge_alter(sll, pll):  # COPIED
    if pll.head is None:  # No PLL. return SLL as is.
        return

    if sll.head is None:  # SLL is none. Make PLL as SLL.
        sll.head = pll.head
        pll.head = None
        return

    stemp = sll.head
    ptemp = pll.head

    while stemp and ptemp:
        snext = stemp.next  # save next node
        pnext = ptemp.next  # save next node of PLL

        stemp.next = ptemp
        if snext: # change pnext only if sll >= pll
            ptemp.next = snext

        stemp = snext
        ptemp = pnext

    pll.head = None
    return

def merge_reverse(s, p):  # COPIED
    ptemp = p.head
    stemp = s.head

    curr = None
    while ptemp or stemp:
        if ptemp and stemp:
            if ptemp.data < stemp.data:
                temp = ptemp
                ptemp = ptemp.next
            else:
                temp = stemp
                stemp = stemp.next
        elif ptemp:
            temp = ptemp
            ptemp = ptemp.next
        else:
            temp = stemp
            stemp = stemp.next

        temp.next = curr
        curr = temp

    sll = Sll()
    sll.head = curr
    p.head, s.head = None, None
    return sll


def create_cycle(sll, k):  # COPIED
    temp = sll.head

    while k:
        k -= 1
        temp = temp.next

    save = temp
    while temp.next:
        temp = temp.next

    print('start of loop is ', save)
    temp.next = save  # created cycle


def detect_cycle(sll):  # COPIED
    if sll.head is None:
        return

    slow = sll.head
    fast = sll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            print('Found loop')
            break
    else: # Dint break. NB NB
        print('No loop')
        return

    count = 1
    slow = slow.next
    while slow is not fast:
        slow = slow.next
        count += 1

    print('Length of loop is: ', count)
    save_count = count

    slow = sll.head
    fast = sll.head
    while count:
        fast = fast.next
        count -= 1

    while slow is not fast:
        slow = slow.next
        fast = fast.next
    print('Loop starts at: ', slow.data)

    # Break loop
    slow = sll.head
    fast = sll.head

    while save_count:
        prev = fast  # save previous of fast
        fast = fast.next
        save_count -=1

    # NB: we saved prev even in the earlier loop because in case of complete circular LL,
    # after previous loop, fast == slow, and hence this loop wont be entered.
    while slow is not fast:
        prev = fast
        fast = fast.next
        slow = slow.next

    prev.next = None
    print(sll)
    return


def check_plaindrome(sll):  # COPIED
    '''
        1. Find midpoint, reverse the second half and match with first half.
         Before returning, restore the sll
        2. Find the midpoint. While doing so, put the first half in a stack
         check the second half against stack
    '''
    stk = LifoQueue()
    if sll.head is None or sll.head.next is None:
        return True

    slow = sll.head
    fast = sll.head

    while fast and fast.next:
        stk.put(slow.data)
        slow = slow.next
        fast = fast.next.next


    if fast:  # Odd number of nodes. move slow over.
        # no need to pop stack as middle element is not added in stack
        slow = slow.next

    while not stk.empty():
        if not slow:
            return False

        if slow.data != stk.get():
            return False
        slow = slow.next
    return True

class Node:  # COPIED
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Queue:  # COPIED
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):  # Insert at tail
        if self.tail == None:  # special case. No elements
            self.tail = Node(data)
            self.head = self.tail  # update head as well
            return

        self.tail.next = Node(data)
        self.tail = self.tail.next

    def pop(self):
        if self.head == None:
            return

        ret = self.head
        self.head = self.head.next
        if self.head is None:  # special case. Last node deletion
            self.tail = None
        return ret.data


def add_two_numbers_given_as_ll(one, two):  # COPIED
    # assume both slls are not empty.
    result = Sll()

    one.reverse()  # reverse number
    two.reverse()  # 1->9->9->3 to 3->9->9->1

    onetmp = one.head
    twotmp = two.head

    carry = 0
    while onetmp or twotmp:
        s = carry
        if onetmp:
            s += onetmp.data
            onetmp = onetmp.next
        if twotmp:
            s+= twotmp.data
            twotmp = twotmp.next
        carry = s//10
        s = s%10
        result.insert_beg(s)
    if carry > 0:
        result.insert_beg(carry)

    one.reverse()
    two.reverse()

    return result


if __name__ == '__main__':
    l = [9, 9, 9, 5, 9, 2, 8]
    sll = Sll()
    for i in l:
        sll.insert_end(i)

    #  sll1.move_even_nodes_end_reverse()
    # sll.reverse()
    # print(sll)
    # print(sll.kth_node_from_last(9))
    pll = Sll()
    l = [8, 4, 8, 1]
    for i in l:
        pll.insert_end(i)

    # pll.merge_sort()
    # sll.merge_sort()
    print(pll)
    print(sll)
    # print('$$$$$$$$$$$$')
    # sll = merge_reverse(sll, pll)
    # sll.sort()
    # print(sll)
    # print('***********')
    ret = add_two_numbers_given_as_ll(sll, pll)
    print(ret)

    # sll.delete_node_given_node(temp)
    # sll.move_last_to_front()
    # sll.move_last_to_front()
    # sll.move_last_to_front()
    # sll.rotate(14)
    # detect_cycle(sll)

    print('------')
    sll.merge_sort()
    # print(sll)
    # sll.reverse()
    # sll.arrange_alternate_highs()
    # print(sll)
    # sll.reverse()
    # print(sll.kth_node_from_last(13))
    # sll.move_last_to_front()
    # print(sll)
    # create_cycle(sll,  12)
    # detect_cycle(sll)

    # sll.arrange_alternate_highs()

    # print(sll)

    sll = Sll()
    for i in [4, 5, 5, 4]:
        sll.insert_end(i)
    print(check_plaindrome(sll))


'''
    print('^^^^^^^^^^^^^')
    q = Queue()
    q.push(1)
    print(q.pop())
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print('#####')
    for i in [10, 11, 12, 13, 14, 15]:
        q.push(i)
        if i %2 == 0:
            print(q.pop())
            q.push(100 + i)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
'''
