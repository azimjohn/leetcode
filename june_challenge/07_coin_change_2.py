class Solution:   
    # Dynamic Programming
    def changeDP(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[-1]

    # Recursion
    def __init__(self):
        self.memo = {}
    
    def changeRec(self, amount: int, coins: List[int]) -> int:
        if (amount, tuple(coins)) in self.memo:
            return self.memo[amount, tuple(coins)]
        
        if amount == 0:
            return 1
    
        if amount < 0 or not coins:
            return 0
        
        result = self.change(amount, coins[:-1]) + self.change(amount-coins[-1], coins)
        self.memo[amount, tuple(coins)] = result
        
        return result
