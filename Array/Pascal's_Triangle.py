#118 Pascal's Triangle
#Difficulty - Easy
#Topic - Array DP
#Time Complexity - O(n^2)
#Space Complexity - O(n^2)

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[]
        for i in range(numRows):
            temp=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1]+res[i-1][j])
                    
            res.append(temp)
        return res 

#Example Usage
sol = Solution()
print(sol.generate(5))  #Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]