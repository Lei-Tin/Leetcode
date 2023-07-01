class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        self.ans = inf
        split = [0] * k

        def solve(i: int):
            if i == n:
                self.ans = min(self.ans, max(split))
                return

            if self.ans <= max(split):
                return

            for j in range(k):
                split[j] += cookies[i]
                solve(i + 1)
                split[j] -= cookies[i]

        solve(0)
        return self.ans
