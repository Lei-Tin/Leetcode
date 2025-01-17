class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {chr(ord('a') + i): [] for i in range(26)}

        for i, char in enumerate(s):
            if len(d[char]) == 0:
                d[char].append(i)
            elif len(d[char]) == 1:
                d[char].append(i)
            else:
                d[char][-1] = i

        ans = 0

        for i in range(26):
            char = chr(ord('a') + i)

            if len(d[char]) == 2:
                l, r = d[char]
                unique_chars = set()

                for k in range(l + 1, r):
                    unique_chars.add(s[k])

                ans += len(unique_chars)

        return ans