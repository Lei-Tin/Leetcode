class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = {}

        for row in matrix:
            inv = tuple(1 - i for i in row)
            r = tuple(row)

            count[inv] = count.get(inv, 0) + 1
            count[r] = count.get(r, 0) + 1

        return max(count.values())

    # Not optimized solution
    #     count = {}

    #     for row in matrix:
    #         val = ''.join(str(i) for i in row)
    #         not_val = self.invert(val)
    #         int_val = int(val, 2)
    #         int_not_val = int(not_val, 2)

    #         count[int_val] = count.get(int_val, 0) + 1
    #         count[int_not_val] = count.get(int_not_val, 0) + 1

    #     return max(count.values())

    # def invert(self, s: str) -> str:
    #     res = ''
    #     for i in s:
    #         if i == '0':
    #             res += '1'
    #         else:
    #             res += '0'

    #     return res

