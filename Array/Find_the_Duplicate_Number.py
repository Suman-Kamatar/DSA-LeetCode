#287 Find the Duplicate Number
#Difficulty - Medium
#Topic - Array Two pointers
#Time complexity- O(n)
#Space complexity - O(1)

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow
    
#example
s = Solution()
print(s.findDuplicate([1,3,4,2,2]))

    
