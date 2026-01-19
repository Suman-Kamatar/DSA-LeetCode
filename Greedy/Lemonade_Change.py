#860 Lemonade Change
#Difficulty - Easy
#Topics = Array Greedy 
#Time Complexity - O(n)
#Space Complexity - O(1)

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=ten=twenty=0

        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if five:
                    ten+=1
                    five-=1
                else:
                    return False
            else:
                if five and ten:
                    five-=1
                    ten-=1
                elif five>=3 and not ten:
                    five-=3
                else:
                    return False
                twenty+=1
        return True
                
#example usage
sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]))  # Output: True