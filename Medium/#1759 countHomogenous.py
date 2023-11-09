class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        curr = ''

        ans = 0
        MOD = 10 ** 9 + 7

        for char in s:
            if curr == char:
                count += 1
                ans += count % MOD
            else:
                curr = char
                count = 1
                ans += 1

        return ans % MOD