class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.check(root, 1)

    def check(root, step):
        if root.left is None and root.right is None:
            return step

        ret = 9999
        if root.left:
            ret = min(ret, self.check(root.left, step + 1))
        if root.right:
            ret = min(ret, self.check(root.right, step + 1))
        return ret


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        ans = 0

        while queue:
            ans += 1
            for i in range(0, len(queue)):
                poll = queue.pop(0)
                if poll.left == None and poll.right == None:
                    return ans
            else:
                if poll.right:
                    queue.append(poll.right)
                if poll.left:
                    queue.append(poll.left)
        return ans
