class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.recSearch(matrix, target, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1))

    def recSearch(self, matrix: List[List[int]], target: int, lu: Tuple[int],
                  rb: Tuple[int]) -> bool:
        # lu is left up, rb is right bottom
        # It is ordered by row, col
        if lu[0] > rb[0] or lu[1] > rb[1]:
            return False

        midRow = (lu[0] + rb[0]) // 2
        midCol = (lu[1] + rb[1]) // 2

        mid = matrix[midRow][midCol]

        # Let matrix be splitted into 4 quadrants
        # 1 2
        # 3 4

        if mid == target:
            return True
        elif mid < target:
            # Then we only search quadrants 2 3 4
            return self.recSearch(matrix, target, (midRow + 1, midCol + 1), rb) \
                or self.recSearch(matrix, target, (lu[0], midCol + 1), (midRow, rb[1])) \
                or self.recSearch(matrix, target, (midRow + 1, lu[1]), (rb[0], midCol))
        else:
            # Then we only search quadrants 1 2 3
            return self.recSearch(matrix, target, lu, (midRow - 1, midCol - 1)) \
                or self.recSearch(matrix, target, (lu[0], midCol), (midRow - 1, rb[1])) \
                or self.recSearch(matrix, target, (midRow, lu[1]), (rb[0], midCol - 1))
