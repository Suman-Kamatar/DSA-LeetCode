#455 Assign Cookies
#Difficulty - Easy
#Topics = Array Greedy Two pointers
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        i=j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count

#example usage
sol = Solution()
print(sol.findContentChildren([1,2,3], [1,1]))  # Output: 1