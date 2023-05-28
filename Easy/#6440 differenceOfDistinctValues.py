class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        ans = [[0 for _ in range(m)] for _ in range(n)]
        for r in range(n):
            for c in range(m):
                top_left = set()
                bottom_right = set()
                r1 = r - 1
                c1 = c - 1

                while r1 >= 0 and c1 >= 0:
                    top_left.add(grid[r1][c1])
                    r1 -= 1
                    c1 -= 1

                r2 = r + 1
                c2 = c + 1
                while r2 < n and c2 < m:
                    bottom_right.add(grid[r2][c2])
                    r2 += 1
                    c2 += 1

                ans[r][c] = abs(len(top_left) - len(bottom_right))

        return ans
