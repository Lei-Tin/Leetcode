class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        last_num = nums[0]

        n = len(nums)
        ans = 0

        for i in range(1, n):
            if nums[i] > last_num:
                # Still ascending
                curr += nums[i]
                last_num = nums[i]
            else:
                ans = max(ans, curr)

                curr = nums[i]
                last_num = nums[i]

        return max(ans, curr)