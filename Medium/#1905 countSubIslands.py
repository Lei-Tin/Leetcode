class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        n, m = len(grid2), len(grid2[0])

        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            res = grid1[i][j] == 1

            for dx, dy in dirs:
                new_x = i + dx
                new_y = j + dy
                if 0 <= new_x < n and 0 <= new_y < m:
                    if (new_x, new_y) in visited:
                        continue

                    if grid2[new_x][new_y] == 1:
                        test = dfs(new_x, new_y)
                        res = res and test

            return res

        ans = 0

        for r in range(n):
            for c in range(m):
                if (r, c) not in visited and grid2[r][c] == 1:
                    if dfs(r, c):
                        ans += 1

        return ans