#121 Best Time to Buy and Sell Stock
#Difficulty - Easy
#Topic -  Array DP
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0; buy=prices[0]

        for pro in prices:
            profit = max(profit,pro-buy)
            buy = min(buy,pro)

        return profit
        
#Example Usage
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))  # Output: 5