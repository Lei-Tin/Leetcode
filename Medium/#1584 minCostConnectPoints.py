class UF:
    def __init__(self, size):
        self.p = {i: i for i in range(size)}
        self.count = 0

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        self.p[xp] = yp

        self.count += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                edges.append((i, j, dist))

        edges.sort(key=lambda x: x[2])

        ans = 0
        djs = UF(n)

        for u, v, cost in edges:
            if djs.union(u, v):
                ans += cost

            if djs.count == n - 1:
                return ans

        return 0
