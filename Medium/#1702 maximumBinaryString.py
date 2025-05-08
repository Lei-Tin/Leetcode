class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Move all ones to the right most
        n = len(binary)
        num_ones = 0
        num_zeros = 0

        leading_ones = True

        for char in binary:
            if char == '1' and leading_ones:
                continue
            if char == '1':
                num_ones += 1
            else:
                leading_ones = False
                num_zeros += 1

        if num_zeros == 0:
            return binary

        return '1' * (n - num_ones - 1) + '0' + '1' * num_ones