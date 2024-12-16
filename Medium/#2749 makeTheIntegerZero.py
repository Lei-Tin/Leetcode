class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ans = 0

        while bin(num1).count('1') > ans:
            num1 -= num2
            ans += 1

            if bin(num1).count('1') <= ans <= num1:
                return ans

        return -1
