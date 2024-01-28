# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # It can only be palindromic if we have a bitmap with at most 1 bit being on
        # We can store this with a 9 bit integer

        def dfs(node: Optional[TreeNode], num: int) -> int:
            if node.left is None and node.right is None:
                # If we are at leaf node
                count = 0

                num ^= 1 << node.val

                # Consider only the bitmap for 1 to 9
                num >>= 1
                for i in range(9):
                    count += (num >> i) & 1

                return int(count == 0 or count == 1)

            ans = 0

            if node.left:
                ans += dfs(node.left, num ^ (1 << node.val))

            if node.right:
                ans += dfs(node.right, num ^ (1 << node.val))

            return ans

        return dfs(root, 0)
