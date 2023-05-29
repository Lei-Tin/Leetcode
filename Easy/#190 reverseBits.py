class Solution:
    def reverseBits(self, n: int) -> int:
        s = self.intToBinary(n)

        s += '0' * (32 - len(s))

        return self.binaryToInt(s)

    def intToBinary(self, n: int) -> str:
        s = ''
        while n > 0:
            s += str(n % 2)
            n = n // 2

        return s

    def binaryToInt(self, s: str) -> int:
        n = 0

        counter = 1

        for i in range(len(s) - 1, -1, -1):
            n += counter * int(s[i])
            counter *= 2

        return n
