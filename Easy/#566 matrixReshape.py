class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        new_mat = [[0 for _ in range(c)] for _ in range(r)]

        row = 0
        col = 0

        i = 0
        j = 0

        while i < len(mat):
            new_mat[row][col] = mat[i][j]

            j += 1
            col += 1

            if col >= c:
                row += 1
                col = 0

            if j >= len(mat[0]):
                i += 1
                j = 0

        return new_mat
