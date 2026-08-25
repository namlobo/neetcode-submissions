# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 or l2 or carry:
            if not l1:
                v1 = 0
            else:
                v1 = l1.val
            if not l2:
                v2 = 0
            else:
                v2 = l2.val
            node = ListNode()
            ans = v1+v2+carry
            digit = ans%10
            carry = ans//10
            node.val = digit
            tail.next = node
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
        