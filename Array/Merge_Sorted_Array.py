#88 Merge Sorted Array
#Difficulty - Easy
#Topic - Array Two Pointers Sorting

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        Time - O(m+n) space - O(m+n)

        temp=[]
        i,j=0,0
        k=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
            k+=1
        while i<m:
            temp.append(nums1[i])
            k+=1;i+=1
        while j<n:
            temp.append(nums2[j])
            k+=1;j+=1
        for i in range(m+n):
            nums1[i]=temp[i]
'''
        #Time - O(m+n) and Space - O(1)
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1
        
#Example Usage
sol = Solution()    
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol.merge(nums1, 3, nums2, 3)
print(nums1)  #Output: [1,2,2,3,5,

