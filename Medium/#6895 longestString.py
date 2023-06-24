class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        self.m = 0

        @cache
        def dp(last: str, i: int, j: int, k: int, l: int):

            if last not in ('AA') and i > 0:
                dp('AA', i - 1, j, k, l + 2)
            if last not in ('AB', 'BB') and j > 0:
                dp('BB', i, j - 1, k, l + 2)
            if last not in ('AA') and k > 0:
                dp('AB', i, j, k - 1, l + 2)

            self.m = max(self.m, l)

        dp('00', x, y, z, 0)
        return self.m
