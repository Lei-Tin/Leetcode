class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        side = len(mat)

        for i in range(side):
            ans += mat[i][i] + mat[i][~i]

        if side % 2 == 1:
            ans -= mat[side // 2][side // 2]

        return ans
