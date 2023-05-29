class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0])

        while start < end:
            mid = (end + start) // 2
            num = matrix[mid // len(matrix[0])][mid % len(matrix[0])]

            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid

        return False
