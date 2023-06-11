# Wasn't able to finish the problem in time
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)

        # Rotating's base cost
        rot = [x * k for k in range(n)]
        for i in range(n):
            num = nums[i]

            for j in range(n):
                # Minimum price that we can get i'th type in each different rotation
                # Either we buy them before any rotation, or we rotate and buy them
                num = min(num, nums[(i + j) % n])
                rot[j] += num

        return min(rot)

        # TLE Solution
#         def dfs(cost: int, types: set, n: List, s: int):
#             if cost > s:
#                 return s

#             if len(types) == len(n):
#                 return cost

#             min_cost = inf
#             for k in range(len(n)):
#                 if k not in types:
#                     cp = types.copy()
#                     cp.add(k)

#                     cp2 = n.copy()
#                     cp2.insert(0, cp2.pop())

#                     min_cost = min(min_cost, dfs(cost + n[k] + x, cp, cp2, s))
#                     min_cost = min(min_cost, dfs(cost + n[k], cp, n, s))

#             return min_cost

#         return dfs(0, set(), nums, sum(nums))
