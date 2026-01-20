#135 Candy
#Difficulty - Hard
#Topics = Array Greedy 
#Time Complexity - O(n)
#Space Complexity - O(n)

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
            
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
        
        return sum(candies)

#example usage
sol = Solution()
print(sol.candy([1,0,2]))  # Output: 5