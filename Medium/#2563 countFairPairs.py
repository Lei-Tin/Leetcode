class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums) - 1):

            num = nums[i]

            # Exclude current num
            left_idx = bisect_left(nums, lower - num, i + 1)
            right_idx = bisect_right(nums, upper - num, i + 1)

            ans += right_idx - left_idx

        return ans
