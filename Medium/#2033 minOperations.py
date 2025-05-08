class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n, m = len(grid), len(grid[0])

        ans = 0

        vals = [grid[i][j] for i in range(n) for j in range(m)]

        vals.sort()

        median = vals[len(vals) // 2]
        for num in vals:
            # Target is to hit median value
            diff = abs(median - num)
            if diff % x != 0:
                return -1
            
            ans += diff // x

        return ans

        