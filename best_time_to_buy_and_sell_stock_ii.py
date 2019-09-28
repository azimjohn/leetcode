# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def maxProfit(prices):
    if not prices:
        return 0

    max_val = min_val = prices[0]
    total_gain = current_gain = 0
    
    for index in range(1, len(prices)):
        if prices[index] < max_val:
            current_gain = max_val - min_val
            total_gain += current_gain
            min_val = prices[index]
        
        max_val = prices[index]

    current_gain = max_val - min_val
    total_gain += current_gain

    return total_gain
