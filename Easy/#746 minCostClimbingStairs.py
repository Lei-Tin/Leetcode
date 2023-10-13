class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}

        for i in range(n):
            dp[i] = min(dp.get(i - 1, 0), dp.get(i - 2, 0)) + cost[i]

        return min(dp.get(n - 1, 0), dp.get(n - 2, 0))
