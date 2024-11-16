class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(0, n - 1, 2):
            char1 = s[i]
            char2 = s[i + 1]

            if char1 != char2:
                ans += 1

        return ans
