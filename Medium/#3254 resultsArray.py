class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Is consecutive
        is_sorted = [nums[i] + 1 == nums[i + 1] for i in range(n - 1)]

        ans = []

        for i in range(n - k + 1):
            if all(is_sorted[i + j] for j in range(k - 1)):
                ans.append(nums[i + k - 1])
            else:
                ans.append(-1)

        return ans
