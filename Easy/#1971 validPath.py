class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = [[] for i in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        q = deque([source])
        visited = set()
        visited.add(source)

        while len(q) > 0:
            curr = q.popleft()

            for neighbor in graph[curr]:
                if neighbor == destination:
                    return True

                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return False
