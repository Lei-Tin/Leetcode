# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lst = self.flatten(root)
        for item in lst:
            tmp = lst.copy()
            tmp.remove(item)
            if k - item in tmp:
                return True

        return False

    def flatten(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        else:
            return self.flatten(root.left) + [root.val] + self.flatten(root.right)
