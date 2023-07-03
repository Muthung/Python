def canCompleteCircuit(gas, cost):
    start = 0
    total = 0
    sum_current = 0

    for i in range(len(gas)):
        different = gas[i] - cost[i]
        total += different
        sum_current += different

        if sum_current < 0:
            start = i + 1
            sum_current = 0

    if total >= 0:
        return start

    return -1
