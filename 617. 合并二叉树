# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        T = TreeNode(0)
        if t1 is not None and t2 is not None:
            T.val = t1.val + t2.val
        else:   
            return t1 if t1 is not None else t2
        if t1.left is not None or t2.left is not None:
            if t1.left is None:
                t1.left = TreeNode(0)
            if t2.left is None:
                t2.left = TreeNode(0)
            T.left = self.mergeTrees(t1.left,t2.left)
        if t1.right is not None or t2.right is not None:
            if t1.right is None:
                t1.right = TreeNode(0)
            if t2.right is None:
                t2.right = TreeNode(0)
            T.right = self.mergeTrees(t1.right,t2.right)
        return T
