# Wasn't able to do this question in time

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        self.ans = 0
        n = len(nums)

        def dfs(u: set, prev: int):
            if len(u) == n:
                self.ans += 1
                return

            for i in range(n):
                if i not in u:
                    if nums[i] % prev == 0 or prev % nums[i] == 0:
                        u_copy = u.copy()
                        u_copy.add(i)

                        dfs(u_copy, nums[i])

        for i in range(n):
            used = set()
            used.add(i)
            dfs(used, nums[i])

        return self.ans
