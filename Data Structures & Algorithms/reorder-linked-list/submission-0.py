# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow = head, head
        # prev= None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #slow would be at middle of linked list and fast would be at end of linked list
        prev,curr = slow,slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while head!=None:
            temp =head.next
            head.next = prev
            nxt = prev.next
            prev.next = temp
            prev = nxt
            head = temp
        return head
            
        