class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = {i: [] for i in range(n)}

        for x, y in roads:
            g[x].append(y)
            g[y].append(x)

        ans = -inf
        for i in range(n):
            for j in range(i + 1, n):
                res = len(g[i]) + len(g[j])
                if i in g[j]:
                    res -= 1

                ans = max(ans, res)

        return ans
