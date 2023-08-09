class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)

        if n == 1:
            return 0

        nums.sort()
        l, r = 0, nums[n - 1] - nums[0]

        while l < r:
            mid = (l + r) // 2

            k = 0
            i = 0
            while i + 1 < n:
                if abs(nums[i] - nums[i + 1]) <= mid:
                    k += 1
                    i += 2
                else:
                    i += 1

            # Even if k == p, we might still be able to reduce r
            if k >= p:
                r = mid
            else:
                l = mid + 1

        return l
