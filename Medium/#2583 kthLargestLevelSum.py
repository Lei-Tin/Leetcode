# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        lvl_sum = {}

        def dfs(node, level):
            if not node:
                return

            lvl_sum[level] = lvl_sum.get(level, 0) + node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        pq = []
        for level in lvl_sum:
            heapq.heappush(pq, -lvl_sum[level])

        if len(lvl_sum) < k:
            return -1

        for j in range(k - 1):
            heapq.heappop(pq)

        return -heapq.heappop(pq)
