#122 Best Time to Buy and Sell II
#Difficulty - Medium
#Topic -  Array DP
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
            
        return profit

#Example Usage
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))  # Output: 7