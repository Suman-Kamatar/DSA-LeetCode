#167 Two Sum II
#Difficulty - Medium
#Topics - Array Two Pointers Binary Search
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

#Example Usage
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Output: [1, 2]