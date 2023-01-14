class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimized solution
        indices = {}

        for i in range(len(nums)):
            if nums[i] in indices:
                # This means we have already seen the
                # complemenet of this value inside the dictionary
                return [indices[nums[i]], i]

            else:
                indices[target - nums[i]] = i

        # Don't need extra return because it is guaranteed to have a solution

        # i = j = 0
        #
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #
        #         j += 1
        #
        #     i += 1
