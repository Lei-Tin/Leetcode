class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.intToBinary(n).count(1)

    def intToBinary(self, n: int) -> list:
        s = []

        while n >= 1:
            s.append(n % 2)
            n = n // 2

        return s
