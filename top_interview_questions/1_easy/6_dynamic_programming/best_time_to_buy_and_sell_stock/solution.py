from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_val = min_val = prices[0]
        max_gain = current_gain = 0

        for index in range(1, len(prices)):

            if prices[index] > max_val:
                max_val = prices[index]
                current_gain = max_val - min_val
                max_gain = current_gain if max_gain < current_gain else max_gain

            if prices[index] < min_val:
                min_val = max_val = prices[index]
                current_gain = 0

        return max_gain
