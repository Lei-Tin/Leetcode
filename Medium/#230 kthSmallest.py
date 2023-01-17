# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []

        self.inOrder(root, path, k)

        return path[k - 1]

    def inOrder(self, root: Optional[TreeNode], path: List[int], k: int) -> None:
        if root is None:
            return

        if len(path) == k:
            return

        self.inOrder(root.left, path, k)
        path.append(root.val)
        self.inOrder(root.right, path, k)

        return
