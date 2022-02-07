from typing import List

class Solution:
    def binary_search(self, nums, start, end, target) -> int:

        if target > nums[end] or target < nums[start]:
            return -1

        index = (end + start) // 2

        if target == nums[index]:
            return index

        elif target > nums[index]:
            return self.binary_search(nums, index + 1, end, target)

        else:
            # targe < nums[index]
            return self.binary_search(nums, start, index - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        return self.binary_search(nums, low, high, target)
