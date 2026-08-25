"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        count = {None:None}#old to copy
        curr = head
        while curr:
            cop = Node(curr.val)#clone the values and add to hashmap
            count[curr] = cop
            curr = curr.next
        curr = head
        while curr:
            cop = count[curr]
            cop.next = count[curr.next]
            cop.random = count[curr.random]
            curr = curr.next
        return count[head]
        