class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    root = [3]

    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1
    print(isBalanced(self, root))
