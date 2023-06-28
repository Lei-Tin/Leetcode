class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = {i: [] for i in range(n)}
        for e, w in zip(edges, succProb):
            g[e[0]].append((e[1], w))
            g[e[1]].append((e[0], w))

        q = deque([(start, 1)])

        visited = {i: 0 for i in range(n)}

        while len(q) > 0:
            n, c = q.popleft()

            if visited[n] > c:
                continue
            else:
                visited[n] = c

            for neighbor, w in g[n]:
                if visited[neighbor] < c * w:
                    q.append((neighbor, c * w))

        return visited[end]
