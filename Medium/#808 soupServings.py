class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0

        d = {}

        def solve(a: int, b: int) -> float:
            if (a, b) in d:
                return d[(a, b)]

            if a > 0 and b <= 0:
                return 0.0
            elif a <= 0 and b <= 0:
                return 0.5
            elif a <= 0 and b > 0:
                return 1.0
            else:
                d[(a, b)] = 0.25 * (solve(a - 100, b) + solve(a - 75, b - 25) + solve(a - 50, b - 50) + solve(a - 25, b - 75))

                return d[(a, b)]

        return solve(n, n)
