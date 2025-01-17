class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stck = []
        for i, num in enumerate(nums):
            if not stck or num < stck[-1][0]:
                stck.append((num, i))

        ans = 0
        n = len(nums)

        for j, num in enumerate(nums[::-1]):
            j = n - j - 1
            while stck and stck[-1][0] <= num:
                ans = max(ans, j - stck.pop()[1])

        return ans