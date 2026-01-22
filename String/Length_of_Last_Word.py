#58 Length of Last Word
#Difficulty - Easy
#Topics = String 
#Time Complexity - O(n)
#Space Complexity - O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  
        return len(s.split()[-1])

# Example usage:
solution = Solution()
result = solution.lengthOfLastWord("   fly me to the moon  ")
print(result)  # Output: 4