## Gas Station 

### Question 

There are *n* gas stations along a circular route, where the amount of gas at the *ith* station is *gas[i]*

You have a car with an unlimited gas tank and it costs *cost[i]* of gas to travel from the *ith* station to its next *(i + 1)th* station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays *gas* and *cost*, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return *-1*. If there exists a solution, it is **guaranteed** to be **unique**.

#### Implementation 

Used the concept of the "Circular tour" problem. The idea is to a running sum of the gas and cost differences while travesring the circular route. If at any point the running sum becomes negative, it means that starting from the current gas station is not feasible. Reset the running sum and start again from the next gas station.

Initialize two variables, *start* - this will keep track of the starting gas station index, and *total* - will keep track of the running sum of gas and cost differences.

Iterate over the gas stations using a for lop with the variable *i *as the index.

Calculate the gas and cost differences at the current gas station by subtracting *cost[i]* from *gas[i]*.
The difference is called *different*.

Add *different* to the *total* variable to update the running sum.

Check if *total* is less than 0. If it is, it means that starting from the current gas station is not feasible. Reset *start* to the next gas station index *i + 1* and reset *total* to 0.

After the loop, check if *total* is greater than or equal to 0. If it is, it means that a feasible starting gas station exist. Return the value of *start*.

If the loop completes without finding a feasible starting gas station, return *-1*.
