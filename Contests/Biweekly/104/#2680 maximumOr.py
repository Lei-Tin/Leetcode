class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums))]
        suffix = [0 for _ in range(len(nums))]

        power = 2 ** k

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] | nums[i - 1]

        for i in range(len(nums) - 1, 0, -1):
            suffix[i - 1] = suffix[i] | nums[i]

        ans = 0

        for i in range(len(nums)):
            ans = max(ans, prefix[i] | nums[i] * power | suffix[i])

        return ans

#         return self.search(nums, k)

#     def search(self, nums: List[int], k: int) -> int:
#         if k == 0:
#             val = nums[0]
#             for i in range(1, len(nums)):
#                 val |= nums[i]

#             return val

#         val = -1
#         for i in range(len(nums)):
#             cp = nums.copy()
#             cp[i] *= 2

#             new_val = self.search(cp, k - 1)
#             if new_val > val:
#                 val = new_val

#         return val
