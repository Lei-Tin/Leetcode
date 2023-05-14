class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()

        graph = {i: [] for i in range(n)}
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        coll = set()
        for v in range(n):
            coll.add(self.bfs(graph, v, seen))

        cnt = 0
        for col in coll:
            if len(col) > 0:
                if self.connected(graph, col):
                    cnt += 1

        return cnt

    def connected(self, g: dict, col: tuple):
        return all(len(g[v]) == len(col) - 1 for v in col)

    def bfs(self, g: dict, start: int, s: set) -> tuple:
        if start in s:
            return tuple()

        q = deque([start])
        s.add(start)

        col = set()
        col.add(start)

        while len(q) > 0:
            v = q.popleft()
            for n in g[v]:
                if n not in s:
                    s.add(n)
                    q.append(n)
                    col.add(n)

        return tuple(sorted(col))
