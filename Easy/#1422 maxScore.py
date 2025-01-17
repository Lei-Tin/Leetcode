class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        pref_left = [0 for _ in range(n + 1)]
        pref_right = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            pref_left[i] = pref_left[i - 1] + int(s[i - 1] == '0')
            pref_right[~i] = pref_right[~(i - 1)] + int(s[~(i - 1)] == '1')

        ans = 0
        for i in range(1, n):
            ans = max(ans, pref_left[i] + pref_right[i])

        return ans