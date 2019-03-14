# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        T = TreeNode(0)
        if root is None: 
            return None
        else:   
            T.val = root.val
            T.left = self.invertTree(root.right)
            T.right = self.invertTree(root.left)
        return T
