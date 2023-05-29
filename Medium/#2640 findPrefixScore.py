class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)

        largest = nums[0]
        conv = [0 for _ in range(n)]
        for i in range(n):
            largest = max(largest, nums[i])
            conv[i] = nums[i] + largest

        ans = [0 for _ in range(n + 1)]
        for i in range(len(conv)):
            ans[i + 1] = ans[i] + conv[i]

        return ans[1:]
