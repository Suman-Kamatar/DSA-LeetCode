#238 Product of Array Except Self
#Difficulty - Medium
#Topics = Array 
#Time Complexity - O(n)
#Space Complexity - O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        prefix=1
        postfix=1
        for i in range(n):
            answer[i]*=prefix
            prefix=nums[i]*prefix
            answer[n-i-1]*=postfix
            postfix=nums[n-1-i]*postfix

        return answer           

#example usage
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]