class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        ans = [-1 for _ in range(n)]
        curr = sum(nums[:2 * k])

        for i in range(k, k + n - 2 * k):
            curr += nums[i + k]

            ans[i] = curr // (2 * k + 1)

            curr -= nums[i - k]

        return ans
