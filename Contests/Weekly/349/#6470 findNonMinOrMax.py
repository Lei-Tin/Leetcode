class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        smallest, largest = min(nums), max(nums)

        for num in nums:
            if num != smallest and num != largest:
                return num

        return -1
