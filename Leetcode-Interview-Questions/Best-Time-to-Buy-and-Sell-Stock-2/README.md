## Best Time to Buy and Sell Stock 2

### Question 

You are given an integer array *prices* where *prices[i]* is the price of a given stock on the *ith* day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it and immediatelysell it on **same day**.

Find and return the **maximum** profit you can achieve.

#### Implementation 

Multiple transactions (buying and selling on the same day) to maximize profits.

Iterate over the prices from the second element to the last element. If the current price is greater than the previous price, add the difference between the two prices to the *maximum_profit*. By doing this, multiple transactions are accounted for and total profit is accumulated.

