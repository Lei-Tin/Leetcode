class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        xor = start ^ goal
        for i in range(32):
            if (xor >> i) & 1 == 1:
                ans += 1

        return ans