# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.search(root, False)

    def search(self, root: Optional[TreeNode], isLeft: bool) -> int:
        if root is None:
            return 0
        # If is leaf and isLeft
        if root.left is None and root.right is None:
            return root.val if isLeft else 0

        return self.search(root.left, True) + self.search(root.right, False)
