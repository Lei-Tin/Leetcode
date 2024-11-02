# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def solve(r1, r2):
            if not r1 and not r2:
                return True

            if r1 and not r2:
                return False

            if r2 and not r1:
                return False

            left_left = solve(r1.left, r2.left)
            left_right = solve(r1.left, r2.right)

            left = left_left or left_right

            right_left = solve(r1.right, r2.left)
            right_right = solve(r1.right, r2.right)

            right = right_left or right_right

            return r1.val == r2.val and (left and right)

        return solve(root1, root2)
