## Container with Most water

### Question 

You are given an integer array *height* of length *n*. There are *n* vertical lines drawn such that the two endpoints of the *ith* line are *(i, 0)* and *(i, height[i])*.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amout of water a container can store.

**Notice** that you may not slant the container.

### Implementation 

Use a two-pointer approach.

Start with two pointers, one at the beginning of the array and the other at the end. The idea is to calculate the area formed by the two lines represented by the pointers and update the maximum area, iterate through the array.

Initialize two pointers, *left* pointing to the start of the array(0), and *right* pointing to the end of the array (n -1).

Initialize a variable *maxArea* to store the maximum area, and set ti to 0.

While *left* is less than *right*:

    Calculate the current area by taking the minimum height between *height[left]* and *height[right]* 
    multiplied by the distance between the two pointers, *right - left*.
    
    Update *maxArea* if the current area is greater then *maxArea*.
    
    Move the pointer with the smaller heightinward. If *height[left]* is smaller, increment *left* by 1;
    otherwise, decrement *right* by 1.
    
After the loop ends, return the value of *maxArea*.
