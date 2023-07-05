class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        ans = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0

        ans = max(ans, prev + curr)

        if all(nums[i] == 1 for i in range(len(nums))):
            return ans - 1

        return ans
