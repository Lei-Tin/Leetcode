class Solution:
    # More optimized solution
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

        return ans

    # Original solution
    # def generate(self, numRows: int) -> List[List[int]]:
    #     if numRows == 1:
    #         return [[1]]
    #
    #     if numRows == 2:
    #         return [[1], [1, 1]]
    #
    #     res = [[1], [1, 1]]
    #
    #     for i in range(3, numRows + 1):
    #         res.append([1] * i)
    #
    #     # Start from row 3 and onwards
    #     for row in range(2, len(res)):
    #
    #         # Start from the second element to the 2nd to the last element
    #         for i in range(1, len(res[row]) - 1):
    #             res[row][i] = res[row - 1][i - 1] + res[row - 1][i]
    #
    #     return res
