# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maxdepth = 0
        # d = 0
        if not root:
            return 0
        #recurisively iterate left subtree and right subtree and then retrun the max depth of that
        l,r = 0,0
        l = 1+ self.maxDepth(root.left)
        r = 1+ self.maxDepth(root.right)
        
        return max(l,r)

        
        