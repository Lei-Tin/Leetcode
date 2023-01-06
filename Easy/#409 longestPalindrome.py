class Solution:
    def longestPalindrome(self, s: str) -> int:
        occur = {}

        for char in s:
            occur[char] = occur.get(char, 0) + 1

        ans = 0

        for char in occur:
            if occur[char] >= 2:
                ans += (occur[char] // 2) * 2

        if any(occur[char] % 2 == 1 for char in occur):
            ans += 1

        return ans
