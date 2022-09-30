class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading white space
        s = s.strip()

        num = 0
        i = 0
        sign = 1

        if s == '':
            return num

        if s[0] == '-':
            sign = -1
            i += 1

        elif s[0] == '+':
            sign = 1
            i += 1

        while i < len(s) and s[i] in '0123456789':
            curr_val = ord(s[i]) - ord('0')
            num = num * 10 + curr_val
            i += 1

        ub = (2 ** 31) - 1
        lb = -(2 ** 31)

        num = sign * num

        if lb <= num <= ub:
            return num
        else:
            if num < lb:
                return lb
            elif num > ub:
                return ub

