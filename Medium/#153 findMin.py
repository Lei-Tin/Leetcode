class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid  # Come in from the right side
            else:
                l = mid + 1

        return nums[l]