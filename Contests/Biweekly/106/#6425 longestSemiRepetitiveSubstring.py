class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        cnt = 0
        start = 0

        while start < len(s):
            cnt = 0
            j = 1

            for i in range(start, len(s) - 1):
                if s[i] == s[i + 1]:
                    cnt += 1

                if cnt == 2:
                    break

                j += 1

            ans = max(ans, j)
            start += 1

        return max(ans, j)
