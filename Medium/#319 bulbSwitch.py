class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Math solution
        i = 1
        while i * i <= n:
            i += 1

        return i - 1

        # Simulation solution
        # bulbs = [0 for _ in range(n)]

        # for i in range(n):
        #     curr = i
        #     while curr < n:
        #         bulbs[curr] = 1 if bulbs[curr] == 0 else 0
        #         curr += i + 1

        # return sum(bulbs)
