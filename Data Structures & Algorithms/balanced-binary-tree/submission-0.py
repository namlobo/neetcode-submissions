# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # 
        def dfs(root):#returns 2 values, if the current sub tree is balanced, and the height of the current subtree
            if not root:
                return [True,0]
            left,right = dfs(root.left),dfs(root.right)
            balanced =(left[0] and right[0] and abs(left[1]-right[1])<=1)
            return [balanced,1+max(left[1],right[1])] #checks if the tree is balanced
        return dfs(root)[0]

        