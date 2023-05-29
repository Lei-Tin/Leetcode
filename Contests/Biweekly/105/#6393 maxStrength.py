class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Optimized solution
        if len(nums) == 1:
            return nums[0]

        ans = 1
        pos = []
        neg = []
        has_zero = False

        for n in nums:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)
            else:
                has_zero = True

        if len(pos) == 0 and has_zero and len(neg) < 2:
            return 0

        for n in pos:
            ans *= n

        neg_sort = sorted(neg)
        i = 0
        j = 1
        while i < len(neg_sort) and j < len(neg_sort):
            ans = ans * (neg_sort[i] * neg_sort[j])
            i += 2
            j += 2

        print(neg_sort)

        return ans


#     # Time limit exceeded
#     def __init__(self):
#         self.highest = -inf
#     def maxStrength(self, nums: List[int]) -> int:
#         dp = {}
#         def prod(curr: Tuple[int]) -> int:
#             if len(curr) == 0:
#                 return -inf
#             if curr in dp:
#                 return dp[curr]

#             ans = 1
#             for i in curr:
#                 ans *= nums[i]

#             dp[curr] = ans
#             return ans

#         def search(curr: Tuple[int]):
#             if len(curr) > len(nums) or curr in dp:
#                 return
#             diff = set(range(len(nums))) - set(curr)
#             power = prod(tuple(sorted(curr)))

#             if power > self.highest:
#                 self.highest = power

#             for i in diff:
#                 new = tuple(sorted(curr + (i, )))
#                 search(new)

#         search(tuple())
#         return self.highest
