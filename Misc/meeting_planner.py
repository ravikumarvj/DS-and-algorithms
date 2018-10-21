### COPIED ###  VERIFIED
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



def overlapping(x, y):
    x1, x2 = x
    y1, y2 = y

    overlap = min(x2, y2) - max(x1, y1)  # negative, if there is no overlap
    return overlap


def merge_time(arr):
    i = 0
    while i < len(arr) - 1: # will len(arr) be calculated for every iteration?
        # print(len(arr))     # Yes, it will.
        if arr[i][1] < arr[i + 1][0]:
            i += 1
        else:
            arr[i] = [arr[i][0], arr[i + 1][1]]
            del arr[i+1]


def find_meeting_time(p1, p2, hours):
    p1.sort(key = lambda x: x[0])
    p2.sort(key = lambda x: x[0])

    merge_time(p1)
    merge_time(p2)

    i, j = 0, 0

    while i < len(p1) and j < len(p2):
        overlap = overlapping(p1[i], p2[j])
        if overlap >= hours:
            return max(p1[i][0], p2[j][0])
        # else:  Cant do this. P1 = 5-25. p2 = 6-15, 16-24
        #     i += 1
        #     j += 1
        elif p1[i][1] < p2[j][1]:
            i += 1
        else:
            j += 1

    return None


if __name__ == '__main__':
    p1 = [[21, 23], [22, 25], [79, 91], [43, 48], [31, 40], [97, 101], [10, 20], [48, 60], [66, 72]]
    p2 = [[42, 50], [12, 15], [60, 72], [18, 22], [76, 95]]

    p1 = [[3, 16]]
    p2 = [[2, 18]]
    print(find_meeting_time(p1, p2, 10))


# 10-20, 21-25, 31-40, 43-60, 66-72, 79-91, 97-101
# 12-15, 18-22, 42-50, 60-72, 76-95



