# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # Option 2: Calculate sum count and do the condition along way
        ans = 0

        def sum_count(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal ans

            if not node:
                return 0, 0

            val = node.val
            count = 1
            left_sum_val, left_count = sum_count(node.left)
            right_sum_val, right_count = sum_count(node.right)

            val += left_sum_val + right_sum_val
            count += left_count + right_count

            if val // count == node.val:
                ans += 1

            return val, count

        sum_count(root)
        return ans

        # Option 1: Calculate sum count and then DFS again
        # def sum_count(node: Optional[TreeNode]) -> Tuple[int, int]:
        #     # Returns sum, count
        #     if not node:
        #         return 0, 0

        #     val = node.val
        #     count = 1

        #     left_sum_val, left_count = sum_count(node.left)
        #     right_sum_val, right_count = sum_count(node.right)

        #     return val + left_sum_val + right_sum_val, count + left_count + right_count

        # def dfs(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0

        #     total, count = sum_count(node)

        #     avg = total // count
        #     ans = 1 if avg == node.val else 0
        #     ans += dfs(node.left)
        #     ans += dfs(node.right)

        #     return ans

        # return dfs(root)