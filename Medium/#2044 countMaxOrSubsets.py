class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)

        max_or = 0
        for num in nums:
            max_or |= num

        @cache
        def dfs(i, curr):
            # Or operation only increases the number, never decreases
            if curr == max_or:
                # Since the value is alrady reached, the rest will only be more subsets (it can never decrease the value or increase)
                return 2 ** (n - i)

            # If curr != max_or
            # And i >= n, this means we are at the end
            # And we chose a subset that doesn't work
            if i >= n:
                return 0

            # Either take or not take the current value
            val = dfs(i + 1, curr | nums[i])
            val += dfs(i + 1, curr)

            return val

        return dfs(0, 0)
