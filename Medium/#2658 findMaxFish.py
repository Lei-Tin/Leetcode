class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = set()

        max_val = -1

        for r in range(height):
            for c in range(width):
                max_val = max(max_val, self.search(grid, r, c, height, width, visited))

        return max_val

    def search(self, grid: List[List[int]], r: int, c: int, height: int, width: int,
               visited: set) -> int:
        if not (0 <= r < height and 0 <= c < width):
            return 0

        if (r, c) in visited:
            return 0

        visited.add((r, c))

        if grid[r][c] == 0:
            return 0

        val = grid[r][c]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            val += self.search(grid, r + dy, c + dx, height, width, visited)

        return val
