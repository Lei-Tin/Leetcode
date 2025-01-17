class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)

        ans = 0

        for k, v in cnt.items():
            if v >= 3 and v % 2 == 1:  # Odd
                ans += 1
            elif v >= 2 and v % 2 == 0:
                ans += 2
            else:
                ans += v

        return ans