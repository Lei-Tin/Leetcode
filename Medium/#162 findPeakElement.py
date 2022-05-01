class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            # Cond 1: If we are at the left most, or, the left neighbor of mid is smaller than mid
            # Cond 2: If we are at the right most, or, the right neighbor of mid is smaller than mid
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (
                    mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid

            # Else case 1: If only 1 of the conditions are satisfied, e.g. mid == 0 or nums[mid] < nums[mid + 1]
            # This is one of the else case because if both the conditions above is satisfied, then we returned something already
            elif mid == 0 or nums[mid - 1] < nums[mid]:
                start = mid + 1

            # Else case 2: If we only satisfy the second condition, that the right neighbor of mid is smaller than mid
            else:
                # Using else also satisfies another condition, such that if mid is smaller than both of its neighbors
                # Then we force the algorithm to look to the left half of this list
                # This works because we know if nums[mid] is lesser than both sides, there must be some index that is a peak to both
                # the left and right of it.

                # E.g. [5,4,3,4,5]
                # Then the peak is both 5s at the left and right
                # E.g. [3,4,3,4,5]
                # Then the peak is 4 to the left.
                # So there must be a peak to the left as well, so we use the else branch to force the code into the left case
                end = mid - 1

        # Cannot find
        return -1

