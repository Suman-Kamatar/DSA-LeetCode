#108 Convert Sorted Array to Binary Search Tree
#Difficulty - Easy
#Topic - Array Divide and Conquer Tree BST 
#Time Complexity - O(n)
#Space Complexity - O(n)

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        # Base case: if the array is empty, return None
        if not nums:
            return None

        # Choose middle element as root (for balance)
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
    
#Example Usage
sol = Solution()
bst_root = sol.sortedArrayToBST([-10,-3,0,5,9])
    

