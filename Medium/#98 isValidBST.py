# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -math.inf, math.inf)

    def isValidBSTHelper(self, root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
        if root is None:
            return True
        elif minimum >= root.val or maximum <= root.val:
            return False
        else:
            return self.isValidBSTHelper(root.left, min(minimum, root.val), root.val) and \
                   self.isValidBSTHelper(root.right, root.val, max(maximum, root.val))
