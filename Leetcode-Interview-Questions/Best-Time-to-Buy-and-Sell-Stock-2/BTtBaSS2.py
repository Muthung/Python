def maxProfit(prices):
    if not prices:
        return 0

    maximum_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maximum_profit += prices[i] - prices[i - 1]

    return maximum_profit
