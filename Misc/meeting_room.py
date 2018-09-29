### COPIED ###

"""
Given a list of meeting times, checks if any of them overlaps. The follow-up question is to return the minimum number of rooms required to accommodate all the meetings.

Let’s start with an example. Suppose we use interval (start, end) to denote the start and end time of the meeting, we have the following meeting times: (1, 4), (5, 6), (8, 9), (2, 6).

In the above example, apparently we should return true for the first question since (1, 4) and (2, 6) have overlaps. For the follow-up question, we need at least 2 meeting rooms so that (1, 4), (5, 6) will be put in one room and (2, 6), (8, 9) will be in the other.

"""

from collections import defaultdict


# Use when meetings are granular
def find_num_rooms(listings):   # Copied
    d = defaultdict(int)       # Space: O(n), where n is the number of hours, over meeting schedule.
                               # Will be large if meetings can be scheduled any minutes

    for meet in listings:
        start, end = meet

        for hr in range(start, end):
            d[hr] += 1

    print(d)
    return max(d.values())


def find_num_rooms_nohash(listings):  # Useful when meetings are in minutes granularity
    listings = sorted(listings, key=lambda x: x[0])  # O(nlogn)

    rooms = []                                   # space: O(no_overlaps) max: O(n)

    for meet in listings:                       # O(n)
        for i in range(len(rooms)):             # worst: O(n) . So total worst O(n^2)
            if rooms[i][1] <= meet[0]:  # Can the meeting be accommodated in room i?
                rooms[i] = meet
                break
        else:  # Din't break out. Add a room
            rooms.append(meet)

    return len(rooms)


def find_num_rooms_nohash(listings):  # Useful when meetings are in minutes granularity
    new_list = []
    for meet in listings:
        new_list.append((meet[0], True))
        new_list.append((meet[1], False))

    new_list = sorted(new_list, key=lambda x: x[0])  # O(nlogn)
    print(new_list)
    count = 0
    max_count = 0
    for item in new_list:
        if item[1] == True:
            if item[0] == 12:
                print(count)
            count += 1
            if count > max_count:
                max_count = count
        else:
            count -= 1

    return max_count

if __name__ == '__main__':
    meetings = ((20, 24), (22, 24), (1, 4), (8, 9), (12, 25), (23, 27), (22, 25), (5, 6), (16, 21), (2, 6), (18, 21), (22, 24))
    ret = find_num_rooms(meetings)
    print(ret)
    ret = find_num_rooms_nohash(meetings)
    print(ret)