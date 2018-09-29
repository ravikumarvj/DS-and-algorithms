#### COPIED #### to Misc
"""
Suppose you are given a chess board and you have only bishops in the chess board (1000000 by 1000000)
We know bishops move digonally ,now you have to tell how many pair of bishops are in attacking position to each other.

Attacking position is defined as-
i) if both the bishops are on the same diagonal then they are in the attacking position.
ii) two bishops can attack each other even if there is a bishop in between them.
"""


def check_attack(first_node, second_node):
    if abs(first_node[0] - second_node[0]) == \
            abs(first_node[1] - second_node[1]):
        return True

    return False


# n is number of bishops and m is row, column in chessboard
# edge_list is position of bishops as tuples.
def find_attacking_bishops(n, m, edge_list):
    count = 0
    for i in range(n):
        # go through all other nodes and check if there is an attack
        for j in range(i, n):
            if i != j:
                if check_attack(edge_list[i], edge_list[j]):
                    count += 1

    return count


from collections import defaultdict
def find_attacking_bishops_hash(n, m, edge_list):
    sum_hash = defaultdict(int)
    dif_hash = defaultdict(int)

    # The bishops are in the same diagonal line,
    # if x+y is same(line like this: /, if top-left corner is (0, 0))
    # or x-y is same (line like: \ .. (0,0), (1,1) .... )
    for x, y in edge_list:
        sum_hash[x+y] += 1
        dif_hash[x-y] += 1

    count = 0
    for i in sum_hash.values():
        count += i*(i-1)//2

    for i in dif_hash.values():
        count += i*(i-1)//2

    return count

edges=[(2, 1), (1, 3), (4, 4), (4, 2), (2, 4), (5, 1)]
print(find_attacking_bishops(6, 6, edges))
print(find_attacking_bishops_hash(6, 6, edges))