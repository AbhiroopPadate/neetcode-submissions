# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        
        if not head.next and n>0:
            return
        
        l = 0

        ptr = head
        h = head
        
        while head:
            l += 1
            head = head.next
        
        if l == n:
            return h.next
        
        for i in range(l-n-1):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return h
        