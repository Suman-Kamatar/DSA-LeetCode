#119 Pascal's Triangle II
#Difficulty - Easy
#Topic - Array DP
#Time Complexity - O(n^2)
#Space Complexity - O(n^2)

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):          
            row = []
            for j in range(i + 1):        
                if j == 0 or j == i:   
                    row.append(1)
                else:
                    row.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        return res[rowIndex]
            
#Example Usage
sol = Solution()
print(sol.getRow(3))  #Output: [1,3,3,1]