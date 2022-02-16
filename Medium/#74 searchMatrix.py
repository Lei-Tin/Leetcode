class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_length = len(matrix[0])

        for row in matrix:
            if target > row[col_length - 1]:
                continue

            return target in row
