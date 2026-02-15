# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        parent = ListNode()
        head = parent
        carry = 0
        while l1 or l2:
            parent.next = ListNode()
            parent = parent.next
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
    
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            
            parent.val = l1_val + l2_val + carry 

            if parent.val > 9:
                carry = 1
                parent.val = parent.val % 10
            else:
                carry = 0
            
            
        if carry > 0:
            child = ListNode(1, None)
            parent.next = child

        return head.next