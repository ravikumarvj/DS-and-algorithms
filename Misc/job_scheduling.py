### COPIED ##   VERIFIED

def find_jobs_profit(arr):
    max_deadline = max((arr[i][1] for i in range(len(arr))))
    slots = [-1] * max_deadline # 0 ==> for deadline 1 and so on

    arr.sort(key=lambda x:x[2], reverse=True) # descending order of profit
    total = 0

    for tpl in arr:
        slot = tpl[1] - 1# find slot

        if tpl[2] <=0: # ignore 0 or negative profit
            continue

        for index in range(slot, -1, -1):  # find a free slot
            if slots[index] == -1:
                slots[index] = tpl[0]  # store the job
                total += tpl[2]
                break

    return total, slots



# All job need a duration of 1 unit. Jobs are given as
# (job-no, deadline in time units, profit-out-of-job)
arr = [(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25), (6, 2, 20),
       (7, 5, 8), (8, 7, 10), (9, 4, 12), (10, 3, 5)]

print(find_jobs_profit(arr))