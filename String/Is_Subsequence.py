#392 Is Subsequence
#Difficulty - Easy
#Topics - String Two Pointers 
#Time Complexity - O(n)
#Space Complexity - O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)
    
#Example Usage
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # Output: True