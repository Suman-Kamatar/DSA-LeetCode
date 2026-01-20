#134 Gas Station
#Difficulty - Medium
#Topics = Array Greedy 
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = index = 0

        for i in range(len(gas)):
            tank+=gas[i]-cost[i]

            if tank < 0:
                tank=0
                index=i+1

        return index

#example usage
sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3