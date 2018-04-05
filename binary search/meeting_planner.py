'''
Implement a meeting planner that can schedule meetings between two persons at a time.
Time is represented by Unix format (also called Epoch) - a positive integer holding the seconds since January 1st, 1970 at midnight.
Planner input:
dur - Meeting duration in seconds (a positive integer).
timesA, timesB - Availability of each person, represented by an array of arrays.
Each sub-array is a time span holding the start (first element) and end (second element) times.
You may assume that time spans are disjointed.  [TODO: If not disjoint, make it disjoint]
Planner output:
Array of two items - start and end times of the planned meeting, representing the earliest opportunity for the two persons to meet for a dur length meeting.
If no possible meeting can be scheduled, return an empty array instead.
'''

#p1 = [[10,20], [21,22], [31,40], [48,60], [66,72], [79, 91]] # [10-20] including 10, but excluding 20
#p2 = [[12,15], [18,22], [42,50], [60,72], [76,95]]

#t1, t2

#t3, t4

#Sorted? sorted
#not disjoint, make it disjoint.
#overlapping? check overlapping time > meeting time.
#If not overlapping increment the one with smallest last time.


def is_overlapping(x, y):
    x1, x2 = x
    y1, y2 = y

    if y1 < x1 < y2 or y1 < x2 < y2:
        return True
    return False


def overlapping_time(x, y):
    x1, x2 = x
    y1, y2 = y

    return min(x2, y2) - max(x1, y1)


def merge(x, y):
    x1, x2 = x
    y1, y2 = y

    return [min(x1, y1), max(x2, y2)]


def merge_time(p):
    b = list()
    b.append(p[0])

    for i in range(1, len(p)):
        if is_overlapping(p[i], b[-1]) or b[-1][1] == p[i][0]:
            m = merge(p1[i], b[-1])
            b[-1] = m
        else:
            b.append(p[i])

    return b


def find_meeting_time(p1, p2, hours):
    p1.sort(key = lambda x: x[0])
    p2.sort(key = lambda x: x[0])


    p1 = merge_time(p1)
    p2 = merge_time(p2)

    # binary search also possible
    i, j = 0, 0
    print(p1)
    print(p2)

    while i < len(p1) and j < len(p2):
        if is_overlapping(p1[i], p2[j]):
            if overlapping_time(p1[i], p2[j]) >= hours:
                return max(p1[i][0], p2[j][0])
            else:
                i += 1
                j += 1
        elif p1[i][1] < p2[j][1]:
            i += 1
        else:
            j += 1

    return None


if __name__ == '__main__':
    p1 = [[21, 23], [22, 25], [79, 91], [43, 48], [31, 40], [97, 101], [10, 20], [48, 60], [66, 72]]
    p2 = [[42, 50], [12, 15], [60, 72], [18, 22], [76, 95]]

    print(find_meeting_time(p1, p2, 8))


# 10-20, 21-25, 31-40, 43-60, 66-72, 79-91, 97-101
# 12-15, 18-22, 42-50, 60-72, 76-95



