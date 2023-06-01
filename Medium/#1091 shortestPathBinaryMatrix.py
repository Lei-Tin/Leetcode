class Solution:
    # TLE Solution, using DFS:
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     if grid[0][0] == 1:
    #         return -1
    #
    #     dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    #     n = len(grid)
    #
    #     def dfs(r: int, c: int, curr: int, visited: set) -> int:
    #         if not (0 <= r < n and 0 <= c < n):
    #             return inf
    #
    #         if r == n - 1 and c == n - 1 and grid[r][c] == 0:
    #             return curr
    #
    #         if grid[r][c] == 1 or (r, c) in visited:
    #             return inf
    #
    #         v = visited.copy()
    #         v.add((r, c))
    #         val = inf
    #
    #         for dr, dc in dirs:
    #             val = min(val, dfs(r + dr, c + dc, curr + 1, v))
    #
    #         return val
    #
    #     Min = dfs(0, 0, 1, set())
    #     if Min == inf:
    #         return -1
    #
    #     return Min

    # BFS Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0:
            return -1

        if n == 1:
            return 1 if grid[0][0] == 0 else -1

        dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        visited = set()
        visited.add((0, 0))
        q = deque([(0, 0, 1)])

        while len(q) > 0:
            r, c, d = q.popleft()
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if not (0 <= new_r < n and 0 <= new_c < n):
                    continue

                if (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    if new_r == n - 1 and new_c == n - 1:
                        return d + 1

                    visited.add((new_r, new_c))
                    q.append((new_r, new_c, d + 1))

        return -1
