# Wasn't able to finish in time
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])

        goodCombs = defaultdict(set)
        maxCombs = 2 ** m

        # We have at most 2 ** num columns possibilities of integers that we can form with rows.
        for i in range(maxCombs):
            for j in range(maxCombs):
                if i & j == 0:
                    goodCombs[i].add(j)

        for i in range(n):
            if all(grid[i][j] == 0 for j in range(m)):
                return [i]

        # Key observation:
        # Why do we only need to check 2 rows?
        positions = {}
        for i in range(n):
            # Notice that as the row is in binary, we can convert it into ints
            rowVal = int(''.join(str(char) for char in grid[i]), 2)

            if rowVal in positions:
                return [positions[rowVal], i]

            for good in goodCombs[rowVal]:
                positions[good] = i

        return []

        # n, m = len(grid), len(grid[0])

        # @cache
        # def dfs(subset: Tuple[int]):
        #     if len(subset) == 0:
        #         return []

        #     colSum = [0 for _ in range(m)]
        #     for j in range(m):
        #         for i in subset:
        #             colSum[j] += grid[i][j]

        #     if all(colSum[i] <= len(subset) // 2 for i in range(m)):
        #         return list(subset)

        #     for i in range(len(subset)):
        #         cp = subset[:i] + subset[i + 1:]

        #         cal = dfs(tuple(sorted(cp)))
        #         if cal != []:
        #             return cal

        #     return []

        # return dfs(tuple(i for i in range(n)))
