class Solution:
    def findComplement(self, num: int) -> int:
        return self.binaryToDec(self.invertBinary(self.decToBinary(num)))

    def decToBinary(self, num: int) -> str:
        s = ''

        while num > 0:
            v = num // 2
            r = num % 2

            num = v

            s += str(r)

        return s[::-1]

    def binaryToDec(self, s: str) -> int:
        res = 0

        for d in range(len(s) - 1, -1, -1):

            if s[d] == '1':
                res += 2 ** (len(s) - d - 1)

        return res

    def invertBinary(self, s: str) -> str:
        res = ''

        for char in s:
            if char == '0':
                res += '1'
            else:
                res += '0'

        return res
