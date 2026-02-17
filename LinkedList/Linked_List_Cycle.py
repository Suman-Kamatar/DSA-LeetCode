#141 Linked List Cycle
#Difficulty - Easy
#Topics - Linked List, Hash Table, Two Poinetrs
#Time Complexity - O(n)
#Space complexity - O(1)

from pyparsing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        a=b=head
        while a!= None and a.next!=None:
            a=a.next.next
            b=b.next
            if a==b:
                return True
        return False
    

# Create a linked list with a cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next  # Creates a cycle

# Check for cycle
sol = Solution()
print(sol.hasCycle(head))  # Output: True

# Create a linked list without a cycle
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)

# Check for cycle
print(sol.hasCycle(head2))  # Output: False

