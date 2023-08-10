class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            while l + 1 < n and nums[l] == nums[l + 1]:
                l += 1
            while r - 1 >= 0 and nums[r] == nums[r - 1]:
                r -= 1

            mid = (l + r) // 2
            val = nums[mid]

            if val == target:
                return True
            # Left is sorted
            elif nums[l] <= val:
                if val >= target and nums[l] <= target:
                    # If target is in left side
                    r = mid - 1
                else:
                    l = mid + 1
            # Right is sorted
            else:
                if val <= target and nums[r] >= target:
                    # If target is in right side
                    l = mid + 1
                else:
                    r = mid - 1

        return False
