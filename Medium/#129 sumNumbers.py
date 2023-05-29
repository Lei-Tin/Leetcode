# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.search(root, 0)
        return self.ans

    def search(self, root: Optional[TreeNode], path: int) -> None:
        if root.left is None and root.right is None:
            self.ans += path * 10 + root.val

        if root.left is not None:
            self.search(root.left, path * 10 + root.val)

        if root.right is not None:
            self.search(root.right, path * 10 + root.val)

