class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.intToBinary(n).count(1) == 1

    def intToBinary(self, n: int) -> list:
        lst = []

        while n > 0:
            lst.append(n % 2)
            n = n // 2

        return lst
