class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = inf

        for i in range(1, n):
            ans = min(ans, nums[i] - nums[i - 1])

        return ans
