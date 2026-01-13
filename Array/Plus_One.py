#66 Plus One
#Difficulty - Easy
#Topic - Array
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
       
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  

        
        return [1] + digits
    
#Example Usage
sol = Solution()    
print(sol.plusOne([1,2,3]))  #Output: [1,2,4]