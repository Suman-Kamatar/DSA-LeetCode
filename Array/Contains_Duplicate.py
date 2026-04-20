#217. Contains Duplicate
#Difficulty - Easy
#Topic - Array Hashtable
#Time Complexity - O(n)
#Space Complexity - O(n)

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

#Example
nums = [1,2,3,1]
print(Solution().containsDuplicate(nums)) #Output - True