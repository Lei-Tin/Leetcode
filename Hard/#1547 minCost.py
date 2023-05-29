class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)

        dp = [[-1 for _ in range(len(cuts))] for _ in range(len(cuts))]

        def solve(i: int, j: int) -> int:
            # Base case is when we cannot cut the stick anymore
            if i + 1 == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            # Otherwise, we try every single possible cutting position
            val = min(solve(i, k) + solve(k, j) for k in range(i + 1, j))

            val += cuts[j] - cuts[i]

            dp[i][j] = val

            return val

        return solve(0, len(cuts) - 1)
