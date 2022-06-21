# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        currA = head
        currB = head
        
        while currA is not None and currB is not None and currB.next is not None:
            currA = currA.next
            currB = currB.next.next
            
            if currA == currB:
                return True
        
        return False
        