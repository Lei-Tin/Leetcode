# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # We have 5 cases here, either
        # 0. Left value is different than right value, then it's automatically False
        # 1. Left is none and right is none, this mean it is symmetrical -> True
        # 2. Left is none and right is NOT NONE, then it is not symmetrical -> False
        # 3. Left is NOT NONE and right is none, then it is not symmetrical -> False
        # 4. Recursive case, left.left is mirror with right.right and left.right is mirror with right.left
        # In case 4, we have to also check if left val is different from right val, if it is different, then we return False

        # Case 1
        if left is None and right is None:
            return True

        # Case 2 and 3 at the same time
        elif left is None or right is None:
            return False

        # Case 4 -> Recursive case
        else:
            if left.val != right.val:
                return False

            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
