class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = 0

        for i in grid:
            for j in i:
                if j > 0:
                    xy += 1

        xz = 0

        for i in grid:
            xz += max(i)

        zy = 0

        zy_rows = []

        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append(grid[j][i])

            zy_rows.append(row)

        zy += sum([max(r) for r in zy_rows])

        return xy + xz + zy
