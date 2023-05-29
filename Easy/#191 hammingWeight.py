class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 2
        count = 0
        while n > 0:
            n &= n - 1
            count += 1

        return count

    #     return self.intToBinary(n).count(1)
    #
    # def intToBinary(self, n: int) -> list:
    #     s = []
    #
    #     while n >= 1:
    #         s.append(n % 2)
    #         n = n // 2
    #
    #     return s
