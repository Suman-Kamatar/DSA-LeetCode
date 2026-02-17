#160 Intersection of Two Linked Lists
#Difficulty - Easy
#Topics - Linked List, Hash Table, Two Poinetrs
#Time Complexity - O(n)
#Space complexity - O(1)

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
                             
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create nodes for the intersecting part
intersecting_node = ListNode(7) 
intersecting_node.next = ListNode(8)

# Create first linked list
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = intersecting_node

# Create second linked list
headB = ListNode(4)
headB.next = ListNode(5)
headB.next.next = intersecting_node

# Find intersection
sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)
if intersection:
    print(f"Intersection at node with value: {intersection.val}")  # Output: Intersection at node with value: 7