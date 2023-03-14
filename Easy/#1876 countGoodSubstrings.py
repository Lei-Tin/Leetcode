class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0

        for l in range(len(s) - 2):
            seen = set()

            for i in range(3):
                seen.add(s[l + i])

            if len(seen) == 3:
                ans += 1

        return ans
