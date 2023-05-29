memorization = {}


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in memorization:
            return memorization[n]

        elif n <= 2:
            memorization[n] = n
            return n

        else:
            ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            memorization[n] = ans
            return ans

