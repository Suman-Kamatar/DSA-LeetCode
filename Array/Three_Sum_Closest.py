#15 3Sum Closest
#Difficulty - Medium
#Topic - Array Two Pointers Sorting
#Time Complexity - O(n^2)
#Space Complexity - O(1)

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  
        return closest_sum

#Example Usage
sol = Solution()
closest = sol.threeSumClosest([-1,2,1,-4], 1)
print(closest)  # Output: 2