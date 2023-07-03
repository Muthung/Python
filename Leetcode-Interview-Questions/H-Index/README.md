## H-index

### Question 

Given an array of integers *citations* where *citations[i]* is the number of citations a researcher received for their *ith* paper, return the researchers' h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of *h* such that the given researcher has published at least *h* papers that have each been cited at least *h* times.

#### Implementation 

Sort the array citations in descending order.

Initialize a variable *h_index* to *0*.

Iterate through the sorted array and for each element, compare it with its index.

> If the element is greater than or equal to the index, increment h_index by 1.
> If the element is less than the index, break out of the loop.

Return the value of h_index.
