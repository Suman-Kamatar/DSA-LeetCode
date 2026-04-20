#53. Maximum Subarray
#Difficulty - Medium
#Topics = Array 
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = float("-inf")

        for num in nums:
            cur_sum = max(num ,cur_sum + num)
            max_sum = max(max_sum ,cur_sum)

        return max_sum
    
#Example 
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums)) #Output - 6
