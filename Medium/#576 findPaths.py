class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i: int, j: int, moves: int) -> int:
            # If out of bounds, return 1
            if (i < 0 or i >= m) or (j < 0 or j >= n):
                return 1

            if moves <= 0:
                return 0

            ans = 0

            for di, dj in dirs:
                ans += dfs(i + di, j + dj, moves - 1) % MOD

            return ans

        return dfs(startRow, startColumn, maxMove) % MOD
