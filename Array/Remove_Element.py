#27 Remove Element
#Difficulty - Easy
#Topic - Array
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j]=nums[i]
                j+=1
        return j
    
#Example Usage
sol = Solution()
print(sol.removeElement([3,2,2,3], 3))  #Output: 2