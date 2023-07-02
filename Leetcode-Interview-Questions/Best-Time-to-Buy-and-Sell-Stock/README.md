## Best Time to Buy and Sell Stock

## Question

You are given an array *prices* where *prices[i]* is the price of a given stock on the *ith* day.

You want to maximize your profit by choosing a **single day** to buy one stock and chosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return *0*.

#### Implementation

Iterate through the array of prices and keep track of the minimum price seen so far and the maximum profit, to maximize the profit from buying and selling stock.

Check if the *prices* array is empty. If it is, return 0 since it can't make any profit.

Initialise the *minimum_price* variable to the price of the first day in the array, and the *maximum_profit* variable to zero.

Iterate through the *prices* array and update the *minimum_price* and *maximum_profit* variables accordingly. For each price, compare it with the current *minimum_price* and update it if the new price is lower. Then, calculate the profit that can be made by sellinng at the current price and subtracting the *minimum_price*. 
If this profit is higher than the current *maximum_profit*, update *maximum_profit* accordingly.

After iterating through all the prices, return the *maximum_profit*.

This algorithm has a time complexity of *0(n)*, where *n* is the length of the *prices* array, need to iterate through all the prices once.
