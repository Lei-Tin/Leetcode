class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid_copy = grid.copy()

        # We will use 0 to denote the land that shouldn't be counted as area

        # Adding an extra column at the very left side and right side of the grid
        for row in grid_copy:
            row.insert(0, 0)
            row.append(0)

        # Adding an extra row in the very end of the grid and the start of the grid
        grid_copy.insert(0, [0] * len(grid[0]))
        grid_copy.insert(len(grid_copy), [0] * len(grid[0]))

        sizes = [0]

        for i in range(len(grid_copy)):
            for j in range(len(grid_copy[0])):
                sizes.append(self.count(grid_copy, i, j))

        return max(sizes)

    def count(self, grid: List[List[int]], row: int, col: int) -> int:
        # We will use 0 to mark as that block shouldn't be counted
        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0

        vertical = self.count(grid, row + 1, col) + self.count(grid, row - 1, col)
        horizontal = self.count(grid, row, col + 1) + self.count(grid, row, col - 1)

        return 1 + vertical + horizontal
