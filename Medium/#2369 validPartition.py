class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n

        for i in range(n + 1):
            if i - 2 >= 0:
                dp[i] = dp[i] or (nums[i - 1] == nums[i - 2] and dp[i - 2])
            if i - 3 >= 0:
                dp[i] = dp[i] or (nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3])
            if i - 3 >= 0:
                dp[i] = dp[i] or (nums[i - 1] - 1 == nums[i - 2] and nums[i - 2] - 1 == nums[i - 3] and dp[i - 3])

        return dp[n]
