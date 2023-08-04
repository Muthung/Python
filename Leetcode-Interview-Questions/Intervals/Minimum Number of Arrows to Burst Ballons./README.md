## Minimum Number of Arrows to Burst Ballons

### Question

There are some spherical balloons taped onto a flat wall that represents the XY-plane. 

The balloons are represented as a 2D integer array *points* where *points[i] = [xstart, xend]* denotes a balloon whose horizontal diameter stretches between *xstart* and *xend*. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 

A balloon with *xstart* and *xend* is **burst** by an arrow shot at *x* if *xstart <= x <= xend*.
 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array *points*, return the minimum number of arrows that must be shot to burst all balloons.

#### Implementation

It can be solved using a greedy algorithm approach. 

The idea is to sort the balloons based on their ending points and then iterate through them, shooting arrows to burst as many balloons as possible with each shot.