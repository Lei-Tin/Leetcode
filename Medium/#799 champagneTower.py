class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = query_row

        rows = [[0] * i for i in range(1, n + 2)]

        rows[0][0] = poured

        # n
        # (n - 1) / 2 in both
        # (((n - 1) / 2) - 1) / 2 in both ends

        for i in range(1, n + 1):
            ends = max((rows[i - 1][0] - 1) / 2, 0)
            rows[i][0] = ends
            rows[i][-1] = ends

            for j in range(1, i):
                rows[i][j] = max((rows[i - 1][j - 1] - 1) / 2, 0) + max((rows[i - 1][j] - 1) / 2, 0)

        return min(rows[query_row][query_glass], 1)
