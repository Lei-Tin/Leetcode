class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = set()
        cols = set()
        ans = 0

        for i in range(len(queries)):
            # Go from back to first
            t, index, v = queries[~i]

            if t == 0:
                # Row
                if index not in rows:
                    rows.add(index)
                    ans += v * n
                    ans -= v * len(cols)

            else:
                # Col
                if index not in cols:
                    cols.add(index)
                    ans += v * n
                    ans -= v * len(rows)

        return ans

    # Simulation failed
#         for t, i, v in queries:
#             if t == 0:
#                 # Row
#                 for c in range(n):
#                     mat[i][c] = v
#             else:
#                 # Col
#                 for r in range(n):
#                     mat[r][i] = v

# return sum(sum(r) for r in mat)
