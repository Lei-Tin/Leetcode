class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_set_bits = bin(num2).count('1')

        ans = 0
        num_used_bits = 0
        for i in range(31, -1, -1):
            if num_used_bits == num_set_bits:
                return ans

            if (num1 >> i) & 1 == 1:
                ans |= 1 << i
                num_used_bits += 1

        i = 0
        while num_used_bits < num_set_bits:
            if (ans >> i) & 1 == 0:
                ans |= 1 << i
                num_used_bits += 1

            i += 1

        return ans