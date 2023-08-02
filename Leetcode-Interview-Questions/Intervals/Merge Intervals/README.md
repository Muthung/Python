## Merge Intervals

### Question 

Given an array of *intervals* where *intervals[i] = [start-i, end-i]*, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#### Implementation 

Sort the intervals based on their start times.

Initialize an empty list to store the merged intervals.

Iterate through the sorted intervals. For each interval:

    - If the merged list is empty or the current interval's start is greater than the end of the last interval in the merged list, add the urrent interval to the merged list.

    - Otherwise, merge the current inerval with the last interval in the merged list by updating the end time of the last interval.

Return the merged list of non-overlapping intervals.