# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stck = []
        if head is None:
            return head
        stck.append(head.val)
        i = head
        while head.next != None:
            stck.append(head.next.val)
            head = head.next
        head = i
        while head.next != None:
            head.val = stck.pop(-1)
            head = head.next
        head.val = stck.pop(-1)
        return i
        
