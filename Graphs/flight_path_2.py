### COPIED ###  VERIFIED
"""
You are going on a one-way indirect flight trip that includes an unknown very large number of transfers.

- You are not stopping twice in the same airport.
- You have 1 ticket for each part of your trip.
- Each ticket contains src and dst airport.
- All the tickets you have are randomly sorted.
- You forgot the original departure airport (very first src) and your destination (last dst).
Design an algorithm to reconstruct your trip with minimum big-O complexity.


- Note:
    Each airport is visited only once. That means there is no loop.
    Every ticket is part of a single journey from src to dst.
    That means all the nodes will for a single chain.
    So, even-though we can do topological sort, there is another method with similar runtime. We are following that
"""


class Node:
    def __init__(self, airport):
        self.airport = airport
        self.next = None


def find_path(flight_list):
    if len(flight_list) <= 0:
        return None

    hash_table = {}
    for start, end in flight_list:
        if start not in hash_table:
            start_node = Node(start)
            hash_table[start] = [1, start_node]
        else:
            start_node = hash_table[start][1]
            del hash_table[start]  # maximum count possible is 2. After which no need to store it in hash
        if end not in hash_table:
            end_node = Node(end)
            hash_table[end] = [1, end_node]
        else:
            end_node = hash_table[end][1]
            del hash_table[end]

        start_node.next = end_node

    # at this point, there should be only two entries in the hash-table. SRC and DST
    print(hash_table)
    if len(hash_table) != 2:
        return None  # No proper path

    start = None
    for src in hash_table.values():
        if src[1].next is not None:
            start = src[1]

    if start is None: # Avoid cases like 1->15, 1->3->5->7. Now hash table will have 15 and 7
        return None
    length = 0
    temp = start
    while temp:
        length += 1
        temp = temp.next

    if length != len(flight_list) + 1:
        return None  # No proper path. This is to avoid 1->2->3, 5->6, 6->5

    while start:
        print(start.airport, end=',')
        start = start.next
    print()


if __name__ == '__main__':
    flights = [(8, 9),(10, 12),(3, 5),(5, 7), (9, 10),(1, 3), (7, 8), (1, 3)]
    find_path(flights)