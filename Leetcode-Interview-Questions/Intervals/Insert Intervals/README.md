## Insert Intervals

### Question

You are given an array of non-overlapping intervals *intervals* where *intervals[i] = [start-i, end-i]* represent the start and the end of the *i-th* interval and *intervals* is sorted in ascending order by *start-i*. 

You are also given an interval *newInterval = [start, end]* that represents the start and end of another interval.

Insert *newInterval* into *intervals* such that *intervals* is still sorted in ascending order by *start-i,* and *intervals* still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return *intervals* after the insertion.

#### Implementation

Iterate through the existing intervals and appropriately merge or insert the new interval.

The function takes the sorted list of intervals and the new interval to be inserted.

It iterates through the intervals, merging overlapping intervals with the new interval, and the returns the merged list of intervals.