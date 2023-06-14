# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []

        def traverse(s: Optional[TreeNode]) -> None:
            if s is None:
                return

            if s.left is not None:
                traverse(s.left)

            l.append(s.val)

            if s.right is not None:
                traverse(s.right)

        traverse(root)
        ans = inf

        for i in range(len(l) - 1):
            ans = min(ans, l[i + 1] - l[i])

        return ans
