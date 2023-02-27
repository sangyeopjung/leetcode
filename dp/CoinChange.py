# https://leetcode.com/problems/coin-change/description/
# tags: dp

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum number of coins needed until amount i
        #       = foreach coin c: min( dp[i-c] + 1 )
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

# recursive: O(k^n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dfs = self.helper(coins, amount, 0)
        return -1 if dfs == float('inf') else dfs

    def helper(self, coins, amount, depth):
        if amount == 0:
            return depth
        
        if amount < 0:
            return float('inf')
        
        dfs = float('inf')
        for coin in coins:
            dfs = min(dfs, self.helper(coins, amount-coin, depth+1))
        
        return dfs