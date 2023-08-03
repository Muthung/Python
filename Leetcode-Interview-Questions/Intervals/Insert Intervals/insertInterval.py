def insert_interval(intervals, newIntervals):
    mergedInt = []
    i = 0
    n = len(intervals)
    
    # Add intervals that come before the new interval
    while i < n and intervals[i][1] < newIntervals[0]:
        mergedInt.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals with the new interval
    while i < n and intervals[i][0] <= newIntervals[1]:
        newIntervals[0] = min(newIntervals[0], intervals[i][0])
        newIntervals[1] = max(newIntervals[1], intervals[i][1])
        i += 1
    
    mergedInt.append(newIntervals)
    
    # Add remaining intervals
    while i < n:
        mergedInt.append(intervals[i])
        i += 1
    
    return mergedInt