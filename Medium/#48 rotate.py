class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Notice that if you reverse the list and then take the transpose,
        # it will be rotated by 90 degrees clockwise

        matrix[:] = matrix[::-1]

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
