# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            qlen = len(queue)
            lev = []
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    lev.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lev:
                res.append(lev)
        return res