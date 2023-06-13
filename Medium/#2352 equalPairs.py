class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Optimized solution, using only 1 dictionary
        rows = {}

        for i in range(n):
            row = tuple(c for c in grid[i])
            rows[row] = rows.get(row, 0) + 1

        ans = 0
        for i in range(n):
            col = tuple(grid[j][i] for j in range(n))
            ans += rows.get(col, 0)

        return ans

        # Brute force
        # rows = {}
        # cols = {}

        # for i in range(n):
        #     row = tuple(c for c in grid[i])
        #     rows[row] = rows.get(row, 0) + 1

        #     col = tuple(grid[j][i] for j in range(n))
        #     cols[col] = cols.get(col, 0) + 1

        # ans = 0
        # for r in rows:
        #     if r in cols:
        #         ans += rows[r] * cols[r]

        # return ans
