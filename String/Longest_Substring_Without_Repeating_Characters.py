#3 Longest Substring Without Repeating Characters
#Difficulty - Medium
#Topics = String Sliding Window
#Time Complexity - O(n)
#Space Complexity - O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            max_len = max(max_len, right-left+1)
        
        return max_len
    
#example
s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))