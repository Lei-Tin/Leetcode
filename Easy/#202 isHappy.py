class Solution:
    def isHappy(self, n: int) -> bool:
        # Using floyd's cycle detection algorithm

        slow = self.magicNum(n)
        fast = self.magicNum(self.magicNum(n))

        while slow != fast:
            slow = self.magicNum(slow)
            fast = self.magicNum(self.magicNum(fast))

        if slow == 1:
            return True

        return False

    def magicNum(self, n: int) -> int:
        val = 0
        while n > 0:
            rem = n % 10
            n //= 10
            val += rem ** 2

        return val
