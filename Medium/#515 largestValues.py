# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS Solution
        if not root:
            return []

        arr = []
        q = deque([(0, root)])

        while q:
            layer, n = q.popleft()

            if layer >= len(arr):
                arr.append(n.val)
            else:
                arr[layer] = max(arr[layer], n.val)

            if n.left:
                q.append((layer + 1, n.left))

            if n.right:
                q.append((layer + 1, n.right))

        return arr

        # DFS Solution
        # arr = []

        # def dfs(r: Optional[TreeNode], layer: int) -> None:
        #     if r is None:
        #         return

        #     if layer >= len(arr):
        #         arr.append(r.val)
        #     else:
        #         arr[layer] = max(arr[layer], r.val)

        #     dfs(r.left, layer + 1)
        #     dfs(r.right, layer + 1)

        # dfs(root, 0)

        # return arr
