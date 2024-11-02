class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        incr = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    incr[i] = max(incr[i], incr[j] + 1)

        return max(incr)
