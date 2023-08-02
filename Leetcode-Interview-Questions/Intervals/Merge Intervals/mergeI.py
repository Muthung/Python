def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged_interval = merged_intervals[-1]
        
        if current_interval[0] > last_merged_interval[1]:
            merged_intervals.append(current_interval)
        else:
            last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
    
    return merged_intervals