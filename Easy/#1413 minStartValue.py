class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefs = [nums[0]]
        neg = nums[0] <= 0
        for i in range(1, len(nums)):
            val = prefs[i - 1] + nums[i]
            prefs.append(val)

            # Negative flag
            if val <= 0:
                neg = True

        if neg:
            return abs(min(prefs)) + 1
        else:
            return 1
