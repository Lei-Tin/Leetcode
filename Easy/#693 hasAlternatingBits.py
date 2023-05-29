class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit_one = bit_two = -1

        while n > 0:
            bit_two = bit_one
            bit_one = n % 2
            n = n // 2

            if bit_two == bit_one:
                return False

        return True
