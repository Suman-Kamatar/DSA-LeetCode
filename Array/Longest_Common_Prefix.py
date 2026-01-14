#14 Longest Common Prefix
#Difficulty - Easy
#Topic - Array and String
#Time Complexity - O(nk)
#Space Complexity - O(1)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

#Example Usage
sol = Solution()    
print(sol.longestCommonPrefix(["flower","flow","flight"]))  #Output: "fl"
