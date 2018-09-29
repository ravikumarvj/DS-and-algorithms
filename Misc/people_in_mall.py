"""
The mall management is trying to figure out what was the busiest moment in the mall in the last year. You are given data from the door detectors: each data entry includes a timestamp (seconds in Unix Epoch format), an amount of people and whether they entered or exited.

Example of a data entry:
{ time: 1440084737,  count: 4,  type: "enter" }

Find what the busiest period was in the mall on the last year. Return an array with two Epoch timestamps representing the beginning and end of that period. You may assume that the data you are given is accurate and that each second with entries or exits is recorded. Implement the most efficient solution possible and analyse its time and space complexity.

"""
# Multiple doors? merge same time?


def convert(array):
    ret = []
    for entry in array:
        if entry[2].lower() == 'exit':
            ret.append([entry[0], -entry[1]])
        else:
            ret.append([entry[0], entry[1]])

    i = 0
    ret.sort()
    while i < len(ret) - 1:
        if ret[i+1][0] == ret[i][0]:
            ret[i][1] += ret[i+1][1]
            del ret[i+1]
        else:
            i += 1

    return ret


def find_max_people(array):
    array = convert(array)
    max_people = 0
    max_start = 0
    max_end = 0
    count = 0

    print(array)
    for i in range(len(array)):
        item = array[i]
        count += item[1]
        if count > max_people:
            max_people = count
            max_start = item[0]
            if i < len(array) - 1:
                max_end = array[i+1][0]
            else:
                max_end = None

    if max_people == 0:  # busiest time was before our start time
        print(max_people, None, array[0][0])
    else:
        print(max_people, max_start, max_end)


if __name__ == '__main__':
    # array = [[18, 5, 'enter'], [32, 6, 'exit'], [20, 4, 'exit'], [18, 3, 'enter'], [35, 3, 'exit'], [21, 1, 'exit'], [20, 1, 'enter'],[24, 4, 'exit'], [21, 5, 'enter'],[30, 14, 'enter'], [32, 5, 'enter'],[26, 4, 'enter']]
    array = [[10, 7, 'Enter'],
             [28, 4, 'Exit'],
             [10, 5, 'Exit'],
             [42, 15, 'Exit'],
             [28, 9, 'Enter'],
             [10, 2, 'Exit'],
             [35, 2, 'Enter'],
             [38, 3, 'Enter'],
             [28, 5, 'Exit'],
             [25, 2, 'Enter'],
             [26, 6, 'Exit'],
             [35, 1, 'Exit'],
             [41, 7, 'Enter'],
             [24, 4, 'Exit'],
             [35, 4, 'Exit']]

    find_max_people(array)

