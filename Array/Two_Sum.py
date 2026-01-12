#1 Two Sum
#Difficulty - Easy
#Topic - Array
#Time Complexity - O(n)
#Space Complexity - O(n)

from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            comp = target-nums[i]

            if comp in seen:
                return [seen[comp],i]

            seen[nums[i]] = i
        
        return -1

#Example Usage
sol = Solution()
print(sol.twoSum([2,7,11,15],9))  #Output: [0,1]