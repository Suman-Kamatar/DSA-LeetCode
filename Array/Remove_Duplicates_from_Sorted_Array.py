#26 Remove Duplicates from Sorted Array
#Difficulty - Easy
#Topic - Array
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                j+=1
                nums[j]=nums[i]
        return j+1
    
#Example Usage
sol = Solution()    
print(sol.removeDuplicates([1,1,2]))  #Output: 2