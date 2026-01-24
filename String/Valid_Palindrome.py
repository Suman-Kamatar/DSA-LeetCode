#125 Valid Palindrome
#Difficulty - Easy
#Topics = String
#Time Complexity - O(n)
#Space Complexity - O(n)

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.strip()
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")
        
        return s == s[::-1]

# Example usage:
solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)  # Output: True