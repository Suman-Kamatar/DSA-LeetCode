#56 Merge Intervals
#Difficulty - Medium
#Topics = Array TwoPointer 
#Time Complexity - O(nlogn)
#Space Complexity - O(n)

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last = merged[-1]
            cur = intervals[i]

            if cur[0] <= last[1]:
                last[1] = max(cur[1], last[1])
            else:
                merged.append(cur)

        return merged

#example
s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))