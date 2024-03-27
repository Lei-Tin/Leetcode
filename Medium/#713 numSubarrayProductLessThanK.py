class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr = nums[0]
        ans = 0
        if curr < k:
            ans += 1

        i, j = 0, 1
        while j < len(nums):
            curr *= nums[j]

            while curr >= k and i <= j:
                curr /= nums[i]
                i += 1

            ans += j - i + 1
            j += 1

        return ans
