class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 0

        n = len(nums)

        i = 0
        j = 0

        while j < n:
            if nums[j] - nums[i] <= 2 * k:
                j += 1
            else:
                i += 1
            ans = max(ans, j - i)

        return ans
