class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        second_high = -1
        high = -1
        idx = 0

        for i in range(len(nums)):
            if nums[i] >= high:
                idx = i
                second_high = high
                high = nums[i]
            elif nums[i] > second_high:
                second_high = nums[i]

        if high >= 2 * second_high:
            return idx
        else:
            return -1
