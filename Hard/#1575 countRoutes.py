class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(curr: int, f: int) -> int:
            if f < 0:
                return 0

            # When we're at the end, we can still go away and come back again
            if curr == finish:
                ans = 1
            else:
                ans = 0

            for i in range(len(locations)):
                if i != curr:
                    ans = ans + dp(i, f - abs(locations[i] - locations[curr]))

            return ans % MOD

        return dp(start, fuel) % MOD
