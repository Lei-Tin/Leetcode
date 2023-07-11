# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)

        def dfs(r: TreeNode) -> None:
            if not r:
                return

            if r.left:
                g[r.val].append(r.left.val)
                g[r.left.val].append(r.val)
                dfs(r.left)

            if r.right:
                g[r.val].append(r.right.val)
                g[r.right.val].append(r.val)
                dfs(r.right)

            return

        # Build graph
        dfs(root)

        ans = []
        q = deque([(target.val, 0)])
        visited = {target.val}

        while q:
            n, d = q.popleft()
            visited.add(n)
            if d == k:
                ans.append(n)
                continue

            for neighbor in g[n]:
                if neighbor not in visited:
                    q.append((neighbor, d + 1))

        return ans

