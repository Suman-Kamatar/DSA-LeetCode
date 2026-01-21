#42 Trapping Rain Water
#Difficulty - Hard
#Topics = Array TwoPointer Dynamic Programming
#Time Complexity - O(n)
#Space Complexity - O(n)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n

        maxLeft = 0
        for i in range(n):
            left[i] = maxLeft
            maxLeft = max(maxLeft, height[i])

        maxRight = 0
        for i in range(n - 1, -1, -1):
            right[i] = maxRight
            maxRight = max(maxRight, height[i])

        water = 0
        for i in range(n):
            trapped = min(left[i], right[i]) - height[i]
            if trapped > 0:
                water += trapped

        return water

#example usage
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6