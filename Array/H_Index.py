#274 H-Index
#Difficulty - Medium
#Topic -  Array Sorting 
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        for i in range(len(citations)):
            papers=len(citations)-i
            if papers<=citations[i]:
                return papers
        
        return 0

#Example Usage
sol = Solution()
citations = [3,0,6,1,5]
print(sol.hIndex(citations))  # Output: 3