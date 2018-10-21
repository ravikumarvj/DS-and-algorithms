### COPIED ###  VERIFIED
"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and
starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.

Note:
    As you can see, the graph can contain cycles. So topological sorting is not an option.
    Another thing to note is that a node (airport) can be visited multiple times.
    Also all flights (edges) must be used. That means we have to 'visit' all edges.
    At each point, we must go through the alphabetically lower edge.
    If a path through that is not possible, we should backtrack
"""
from collections import defaultdict


def _print_path(start, edge_list, edge_dict, visited, result):
    if len(visited) == len(edge_list):  # If all edges are visited, we are done
        return True

    for end in edge_dict[start]:
        if (start, end) in visited:  # Ignore any visited edge
            continue
        visited.add((start, end))
        result.append(end)

        if _print_path(end, edge_list, edge_dict, visited, result):
            return True
        else:
            visited.remove((start, end))
            result.pop()
    return False

def pre_process(edge_dict, edge_list):
    edge_list.sort()  # Sort the list as we need neighbours in lexicographical order
    for flight in edge_list:
        start, end = flight
        edge_dict[start].append(end)  # Creating dict of lists

def print_path(edge_list, start):  # edge_list is list of tuples
    edge_dict = defaultdict(list)  # Create a default dict to create a neighbour list
    visited = set()  # Keeps track of visited edges
    pre_process(edge_dict, edge_list)  # From the edge list, create neighbour list
    result = [start]

    ret = _print_path(start, edge_list, edge_dict, visited, result)
    print(ret, result)



if __name__ == '__main__':
    # flight_list = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('A', 'C'), ('C', 'A'), ('C', 'B')]
    # print_path(flight_list, 'A')
    flight_list = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    print_path(flight_list, 'A')