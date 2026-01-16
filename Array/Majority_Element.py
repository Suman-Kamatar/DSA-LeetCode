#169 Majority Element
#Difficulty - Easy
#Topic - Array Divide and Conquer Hash table 
#Time complexity- O(n)
#Space complexity - O(n)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq ={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,value in freq.items():
            if value >= len(nums)/2:
                return key
        return -1

        
#Example Usage
sol = Solution()
majority = sol.majorityElement([3,2,3])
print(majority)  # Output: 3