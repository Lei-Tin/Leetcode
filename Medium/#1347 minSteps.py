class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = [0] * 26
        n = len(s)

        for i in range(n):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1

        ans = 0
        for i in range(26):
            if arr[i] > 0:
                ans += arr[i]

        return ans