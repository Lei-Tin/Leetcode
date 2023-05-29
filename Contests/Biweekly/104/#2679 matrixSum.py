class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        height = len(nums)
        size = len(nums[0])

        for i in range(height):
            nums[i].sort(reverse=True)

        ans = 0

        for i in range(size):
            max_val = -1
            for j in range(height):
                max_val = max(nums[j][i], max_val)

            ans += max_val

        return ans
