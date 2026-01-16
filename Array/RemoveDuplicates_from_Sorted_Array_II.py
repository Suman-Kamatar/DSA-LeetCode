#80 Remove Duplicates from Sorted Array II
#Difficulty - Medium
#Topic - Array Two pointers
#Time complexity- O(n)
#Space complexity - O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        count=0

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count+=1
                if count<2:
                    nums[k]=nums[i]
                    k+=1
            else:
                nums[k]=nums[i]
                k+=1
                count=0

        return k

#Example Usage
sol = Solution()
length = sol.removeDuplicates([1,1,1,2,2,3])
print(length)  # Output: 5