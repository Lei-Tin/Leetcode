class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        d = defaultdict(list)

        maxR = [0 for _ in range(n)]
        maxC = [0 for _ in range(m)]
        tmpR, tmpC = maxR[:], maxC[:]

        for r in range(n):
            for c in range(m):
                d[mat[r][c]].append((r, c))

        for val in sorted(d, reverse=True):
            for r2, c2 in d[val]:
                largest = max(maxR[r2], maxC[c2])
                tmpR[r2] = max(tmpR[r2], largest + 1)
                tmpC[c2] = max(tmpC[c2], largest + 1)

            for r2, c2 in d[val]:
                maxR[r2] = tmpR[r2]
                maxC[c2] = tmpC[c2]

        return max(max(maxR), max(maxC))
