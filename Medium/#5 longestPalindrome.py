class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''

        for i in range(len(s)):
            odd = self.extendPalindrome(s, i, i)
            even = self.extendPalindrome(s, i, i + 1)

            longer = odd if len(odd) > len(even) else even

            if len(longer) > len(ans):
                ans = longer

        return ans

    def extendPalindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]
