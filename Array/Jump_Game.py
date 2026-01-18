#55 Jump Game
#Difficulty - Medium
#Topic -  Array DP Greedy
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump=0
        
        for i in range(len(nums)):

            if maxJump<i:
                return False
            maxJump=max(maxJump,i+nums[i])
            if maxJump>=len(nums):
                return True

        return True
    
#Example Usage
sol = Solution()
nums = [2,3,1,1,4]
print(sol.canJump(nums))  # Output: True