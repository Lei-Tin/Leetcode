class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = {}
        nums.sort()

        for n in nums:
            sqrt = math.sqrt(n)

            if int(sqrt) != sqrt:
                seen[n] = 1
            else:
                int_sqrt = int(sqrt)

                if int_sqrt in seen:
                    seen[n] = seen[int_sqrt] + 1
                else:
                    seen[n] = 1

        max_val = max(seen.values())

        return max_val if max_val != 1 else -1


# Union find solution
class UF:
    def __init__(self, vals):
        self.p = {i: i for i in vals}

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        self.p[xp] = yp
        return True

# class Solution:
#     # UF Solution
#     def longestSquareStreak(self, nums: List[int]) -> int:
#         # Init UF
#         # Each entry is connecting to itself
#         uf = UF(nums)
#
#         for num in nums:
#             # Union its sqrt and its square
#             sqrt_num = math.sqrt(num)
#             if sqrt_num == int(sqrt_num) and int(sqrt_num) in uf.p:
#                 uf.union(num, sqrt_num)
#
#             sq_num = int(num ** 2)
#             if sq_num in uf.p:
#                 uf.union(num, sq_num)
#
#         counts = {}
#         for n in uf.p:
#             val = uf.find(n)
#             counts[val] = counts.get(val, 0) + 1
#
#         ans = max(counts.values())
#
#         return -1 if ans == 1 else ans
