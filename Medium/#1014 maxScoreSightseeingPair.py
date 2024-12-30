class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = -1
        max_val = -1

        for i, num in enumerate(values):
            ans = max(ans, max_val + num)

            # Decrement per step because it has been further
            max_val = max(max_val, num) - 1

        return ans
