## Trapping Rain water

### Question 

Given *n* non-negative integers representing an elevation map where the width of each bar is *1*, compute how much water it can trap after raining.

#### Implementation 

Using Two-pointer approach. Initialize two pointers, left and right, at the beginning and end of the elevation map, respectively. Maintain two variables, *left_maxim* and *right_maxim*, to keep track of the maximum height encountered from the left and right sides, respectively.

Iterate through the elevation map using the two pointers and update the *left_maxim* and *right_maxim* values accordingly. At each position, calculate the amount of water that can be trapped based on the minimum of the *left_maxim* and *right_maxim* heights. If the current height is less then the minimum, add the difference between the minimum and the current height to the total amount of trapped water.

Iterate left pointer to *0*, right pointer to *n - 1*, *left-maxim* to *0*, *right_maxim* to *0*, and water_total to *0*.

While the left pointer is less than or equal to the right pointer:

    (a) If height[left] is less than or equal to height[right]:
    
        If height[left] is less than left_maxim, update left_maxim to height[left].
    
        Otherwise, calculate the water trapped by adding left_maxim - height[left] to water_total.
    
        Increment the left pointer.
    
    (b) If height[left]is greater than height[right]:
        
        If height[right] is greater than right_maxim, update right_maxim to height[right].
        
        Otherwise, calculate the water trapped by adding right_maxim - height[right] to water_total.
        
        Decrement the right pointer.
        
    (c) Return the water_total.
