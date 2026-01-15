#11 Container With Most Water
#Difficulty - Medium
#Topic - Array Two Pointers Greedy
#Time Complexity - O(n)
#Space Complexity - O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, h * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


#Example Usage
sol = Solution()
area = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(area)  # Output: 49