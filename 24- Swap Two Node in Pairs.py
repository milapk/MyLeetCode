# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy.next
        if l:
            r = l.next
        while l and r:
            temp = r.val
            r.val = l.val
            l.val= temp

            
            l = r.next
            if l:
                r = l.next
            
        return dummy.next