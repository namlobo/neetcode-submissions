# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dia = 0
        # l,r = 0,0
        # if not root:
        #     return None
        # l = 1+self.diameterOfBinaryTree(root.left)
        # r = 1+self.diameterOfBinaryTree(root.right)
        # dia = max(dia,l+r)
        self.res = 0
        #return height
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res,left+right)
            return max(left,right)+1
        dfs(root)
        return self.res