class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        right = l - 1

        if nums[right] != target:
            return [-1, -1]

        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        left = l

        return [left, right]
