#45 Jump Game II
#Difficulty - Medium
#Topic -  Array DP
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        curEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == curEnd:
                steps += 1
                curEnd = farthest

        return steps

#Example Usage
sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))  # Output: 2