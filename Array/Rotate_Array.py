#189 Rotate Array
#Difficulty - Medium
#Topic - Array Two pointers
#Time complexity- O(n)
#Space complexity - O(n)

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        def reverse(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

        k=k%len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        
#Example Usage
sol = Solution()    
arr = [1,2,3,4,5,6,7]
k = 3   
sol.rotate(arr, k)
print(arr)  # Output: [5,6,7,1,2,3,4]