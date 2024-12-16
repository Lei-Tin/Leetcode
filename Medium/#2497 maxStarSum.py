class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = {}
        for u, v in edges:
            if vals[v] > 0:
                g.setdefault(u, []).append(vals[v])
            if vals[u] > 0:
                g.setdefault(v, []).append(vals[u])

        for u in g:
            g[u] = sorted(g[u], reverse=True)

        n = len(vals)

        max_sum = -float('inf')

        for node in range(n):
            n_score = sum(g.get(node, [])[:k])

            max_sum = max(max_sum, vals[node] + n_score)

        return max_sum
