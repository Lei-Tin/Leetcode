class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        s = 0
        num_neg = 0
        min_val = float('inf')

        zero_flag = False

        for row in matrix:
            for item in row:
                if item == 0:
                    zero_flag = True

                if item < 0:
                    num_neg += 1

                s += abs(item)

                min_val = min(abs(item), min_val)

        return s - 2 * min_val if num_neg % 2 == 1 and not zero_flag else s
