#28  Find the Index of the First Occurrence in a String
#Difficulty - Easy
#Topics = String
#Time Complexity - O(n)
#Space Complexity - O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1

# Example usage:
solution = Solution()
result = solution.strStr("hello", "ll")
print(result)  # Output: 2