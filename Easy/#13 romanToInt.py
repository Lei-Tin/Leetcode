class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = r[s[0]]

        for i in range(1, len(s)):
            if r[s[i]] <= r[s[i - 1]]:
                ans += r[s[i]]

            else:
                ans = ans - r[s[i - 1]] + r[s[i]] - r[s[i - 1]]

        return ans
