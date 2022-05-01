class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

                j += 1

            i += 1
