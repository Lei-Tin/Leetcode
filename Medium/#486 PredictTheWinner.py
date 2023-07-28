class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # solve() returns score of player 1 - score of player 2
        @cache
        def solve(i: int, j: int) -> int:
            if i >= j:
                return nums[i]

            return max(nums[i] - solve(i + 1, j), nums[j] - solve(i, j - 1))

        return solve(0, len(nums) - 1) >= 0
