class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(grid), len(grid[0])

        for c in range(m):
            largest = -inf
            smallest = inf
            for r in range(n):
                largest = max(largest, grid[r][c])
                smallest = min(smallest, grid[r][c])

            if len(str(largest)) > len(str(smallest)):
                ans.append(len(str(largest)))
            else:
                ans.append(len(str(smallest)))

        return ans

