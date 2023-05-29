class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build the graph
        graph = {}

        for edge in edges:
            s, e = edge
            graph[s] = graph.get(s, []) + [e]
            graph[e] = graph.get(e, []) + [s]

        ans = self.dfs(graph, 0, {0}, hasApple)

        return max(ans - 2, 0)

    def dfs(self, graph: dict, start: int, seen: set, hasApple: List[bool]) -> int:
        res = 0

        for neighbor in graph[start]:
            if neighbor not in seen:
                new_seen = seen.copy()
                new_seen.add(neighbor)

                res += self.dfs(graph, neighbor, new_seen, hasApple)

        # This is the case where we have found an apple down there, because res is not 0
        # If we have found an apple right here, then we can add 2 to the result right now
        if res != 0 or hasApple[start]:
            return res + 2

        return res

