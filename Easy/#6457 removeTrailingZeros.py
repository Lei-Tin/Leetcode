class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        s = [char for char in num]
        i = len(num) - 1
        while i >= 0 and s[i] == '0':
            s.pop(i)
            i -= 1

        return ''.join(s)
