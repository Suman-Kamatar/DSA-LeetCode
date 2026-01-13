#35 Search Insert Position
#Difficulty - Easy
#Topic - Array
#Time Complexity - O(log n)
#Space Complexity - O(1)

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

#Example Usage
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))  #Output: 2