def maxProfit(prices):
    if not prices:
        return 0

    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices:
        minimum_price = min(minimum_price, price)
        maximum_profit = max(maximum_profit, price - minimum_price)

    return maximum_profit
