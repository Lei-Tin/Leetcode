class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(i: int, curr_val: int):
            if i >= n:
                return curr_val == target

            # Take minus
            ans = solve(i + 1, curr_val - nums[i])

            # Take plus
            ans += solve(i + 1, curr_val + nums[i])

            return ans

        return solve(0, 0)
