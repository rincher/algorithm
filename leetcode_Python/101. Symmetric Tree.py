# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is not None and right is None:
            return False
        if left is None and right is not None:
            return False
        a = self.check(left.left, right.right)
        b = self.check(left.right, right.left)
        return a and b
