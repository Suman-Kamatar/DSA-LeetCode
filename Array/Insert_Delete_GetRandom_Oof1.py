#380 Insert Delete GetRandom O(1)
#Difficulty - Medium
#Topic -  Array Hash Table 
#Time Complexity - O(1)
#Space Complexity - O(n)

import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.arr.append(val)
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # swap with last
        self.arr[idx] = last
        self.pos[last] = idx

        # remove last
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

#Example Usage
randomSet = RandomizedSet()
print(randomSet.insert(1))    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomSet.remove(2))    # Returns false as 2 does not exist in the set.
print(randomSet.insert(2))    # Inserts 2 to the set, returns true.     
print(randomSet.getRandom())  # getRandom should return either 1 or 2 randomly.
print(randomSet.remove(1))    # Removes 1 from the set, returns true.
print(randomSet.insert(2))    # 2 was already in the set, so return false.
print(randomSet.getRandom())  # Since 2 is the only number in the set,
