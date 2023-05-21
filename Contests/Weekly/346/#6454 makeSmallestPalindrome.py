# Wasn't able to do this question in time
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s) // 2):
            if s[i] < s[~i]:
                ans += s[i]
            else:
                ans += s[~i]
        if len(s) % 2 == 0:
            return ans + ans[::-1]
        else:
            return ans + s[len(s) // 2] + ans[::-1]
