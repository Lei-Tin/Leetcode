class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()

        @cache
        def solve(i: int, prev: int) -> int:
            if i == n:
                return 0

            ans = -1

            # This is pick
            if pairs[i][0] > prev:
                ans = 1 + solve(i + 1, pairs[i][1])

            # This is not pick
            return max(ans, solve(i + 1, prev))

        return solve(0, -inf)
