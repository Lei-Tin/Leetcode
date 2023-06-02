class Solution:

    # Optimized DFS Solution:
    class Solution:
        def maximumDetonation(self, bombs: List[List[int]]) -> int:
            val = -inf
            g = defaultdict(list)

            for i in range(len(bombs)):
                x, y, r = bombs[i]
                for j in range(len(bombs)):
                    if i != j:
                        x2, y2, r2 = bombs[j]
                        if (x2 - x) ** 2 + (y2 - y) ** 2 <= r ** 2:
                            g[i].append(j)

            def dfs(i: int, visited: set):
                visited.add(i)
                for neighbor in g[i]:
                    if neighbor not in visited:
                        dfs(neighbor, visited)

            for i in range(len(bombs)):
                visited = set()
                dfs(i, visited)
                val = max(val, len(visited))

            return val

    # Naive solution that was accepted
    # def maximumDetonation(self, bombs: List[List[int]]) -> int:
    #     val = -inf
    #
    #     def detonate(i: int, detonated: set) -> int:
    #         detonated.add(i)
    #         count = 1
    #
    #         x, y, r = bombs[i]
    #
    #         for j in range(len(bombs)):
    #             if j not in detonated:
    #                 x2, y2, r2 = bombs[j]
    #                 if (x2 - x) ** 2 + (y2 - y) ** 2 <= r ** 2:
    #                     count += detonate(j, detonated)
    #
    #         return count
    #
    #     for i in range(len(bombs)):
    #         exploded = set()
    #         val = max(val, detonate(i, exploded))
    #
    #     return val
