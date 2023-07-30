class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @cache
        def solve(i: int, j: int) -> int:
            if i == j:
                return 1

            ans = inf
            for k in range(i, j):
                ans = min(ans, solve(i, k) + solve(k + 1, j))

            return ans - 1 if s[i] == s[j] else ans

        return solve(0, n - 1)
