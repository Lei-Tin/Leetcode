class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        positives = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    break
                positives += 1

        return m * n - positives

        # num_neg = 0
        #         curr_col = len(grid[0])

        #         for i in range(len(grid)):
        #             for j in range(curr_col):
        #                 if grid[i][j] < 0:
        #                     num_neg += (len(grid) - i) * (curr_col - j)
        #                     curr_col = j

        #                     break

        # Binary search method

    #     curr_col = len(grid[0])
    #     rows = len(grid)
    #
    #     for idx in range(len(grid)):
    #         i = self.binarySearch(grid[idx], curr_col)
    #         num_neg += (rows - idx) * (curr_col - i)
    #
    #         curr_col = i
    #
    #     return num_neg
    #
    # # Binary search method
    # def binarySearch(self, lst: List[int], end: int) -> int:
    #     """Returns the index of the first negative number in the a reversely sorted lst using binary search"""
    #     start = 0
    #
    #     while start < end:
    #         mid = start + (end - start) // 2
    #
    #         if lst[mid] < 0:
    #             end = mid
    #
    #         else:
    #             start = mid + 1
    #
    #     return start
