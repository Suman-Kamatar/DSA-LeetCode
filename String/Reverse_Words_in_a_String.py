#151 Reverse Words in a String
#Difficulty - Medium
#Topics = String 
#Time Complexity - O(n)
#Space Complexity - O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])

        return " ".join(res)

# Example usage:
solution = Solution()
result = solution.reverseWords("  hello world  ")
print(result)  # Output: "world hello"