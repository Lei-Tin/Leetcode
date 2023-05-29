# Wasn't able to solve in time
class Solution:
    def minimumCost(self, s: str) -> int:
        cost = 0
        n = len(s)
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                cost += min(i + 1, n - i - 1)

        return cost
