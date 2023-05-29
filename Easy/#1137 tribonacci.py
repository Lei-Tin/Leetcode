class Solution:
    def tribonacci(self, n: int) -> int:
        return self.getTribonacci(n, {0: 0, 1: 1, 2: 1})

    def getTribonacci(self, n: int, vals: dict) -> int:
        if n in vals:
            return vals[n]
        else:
            val = self.getTribonacci(n - 1, vals) + self.getTribonacci(n - 2, vals) + self.getTribonacci(n - 3, vals)
            vals[n] = val

            return val
