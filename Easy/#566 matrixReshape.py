class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        new_mat = []

        flatten_mat = self.flatten(mat)

        for row in range(r):
            column = []
            for col in range(c):
                column.append(flatten_mat[row * c + (col)])

            new_mat.append(column)

        return new_mat

    def flatten(self, mat: List[List[int]]) -> List[int]:
        return [item for sublist in mat for item in sublist]
