# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        mp = {}

        def dfs(node: Optional[TreeNode], level: int, dump: bool):
            if not node:
                return

            # At odd
            if level % 2 == 1:
                if not dump:
                    mp.setdefault(level, []).append(node.val)
                else:
                    curr_stack = mp[level]
                    node.val = curr_stack.pop()

            dfs(node.left, level + 1, dump)
            dfs(node.right, level + 1, dump)

        dfs(root, 0, False)
        dfs(root, 0, True)

        return root
