class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # One liner solution
        # return [i for i in range(len(nums)) if sorted(nums)[i] == target]

        # Optimized solution
        lessthan = 0
        equal = 0

        for num in nums:
            if num < target:
                lessthan += 1
            elif num == target:
                equal += 1

        return [i for i in range(lessthan, lessthan + equal)]
