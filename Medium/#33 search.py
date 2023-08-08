class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        # Find the rotation index using binary search
        while l < r:
            mid = (l + r) // 2
            val = nums[mid]

            if val > nums[r]:
                l = mid + 1
            else:
                r = mid

        rot = l

        # Find the value using rotation
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2
            val = nums[(mid + rot) % n]

            if val == target:
                return (mid + rot) % n
            elif val > target:
                r = mid
            else:
                l = mid + 1

        return -1
