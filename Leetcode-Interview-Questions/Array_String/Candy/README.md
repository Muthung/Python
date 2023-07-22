## Candy

### Question 

There are *n* children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
    
    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.
    
Return the minimum number of candies you need to have to distribute the candies to the children.

#### Implementation 

Used a Greedy Algorithm. Iterate through the ratings array twicw, once from left to right and once from right to left.

In the first iteration, initialize an array called *candies* with all elements set to *1*. This ensures that each child has at least one candy.

Then, starting from the second child, if the current child has a higher rating than the previous child, assign one more candy to the current child compared to the previous child. This step ensures that children with a higher rating get more candies than their neighbors on the left.

In the second iteration, compare each child with its right neighbor. If the current child has a higher rating than the next child but has fewer or equal candies, assign one more candy to the current child than the next child. This step ensures that children with a higher rating get more candies than their neighbors on the right.

Finally, sum up the elements of the *candies* array to get the minimum number of candies required.
