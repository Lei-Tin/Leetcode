class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Go from the reverse order because this special number is usually larger?
        for i in range(len(nums), 0, -1):
            if sum(j >= i for j in nums) == i:
                return i

        return -1
