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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Sort edges by increasing cost and keeping the original index
        sorted_edges = sorted(zip(edges, range(len(edges))), key=lambda x: x[0][2])

        def get_mst_without_edge(edge: int) -> int:
            s = UF(n)

            ind = 0
            res = 0

            # While not a full spanning tree
            while ind < len(edges) and s.count != n - 1:
                # Add an edge
                (u, v, c), i = sorted_edges[ind]

                if edge != i:
                    if s.union(u, v):
                        res += c

                ind += 1

            return res if s.count == n - 1 else inf

        def get_mst_with_edge(edge: int) -> int:
            s = UF(n)

            ind = 0
            u, v, c = edges[edge]
            s.union(u, v)

            res = c

            # While not a full spanning tree
            while s.count < n - 1:
                # Add an edge
                (u, v, c), i = sorted_edges[ind]

                if edge != i:
                    if s.union(u, v):
                        res += c

                ind += 1

            return res

        # Get minimum possible cost
        min_cost = get_mst_without_edge(-1)

        critical = []
        p_critical = []

        for i in range(len(edges)):
            cost = get_mst_without_edge(i)

            if cost > min_cost:
                critical.append(i)
            else:
                cost_with = get_mst_with_edge(i)
                if cost_with == min_cost:
                    p_critical.append(i)

        return [critical, p_critical]
