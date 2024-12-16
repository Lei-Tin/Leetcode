class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Simulation solution
        # n = len(nums)

        # ans = 0

        # for i in range(n):
        #     if nums[i] == 0:
        #         # Begin simulation
        #         for d in (-1, 1):
        #             nums_cp = nums[:]
        #             j = i

        #             # While in range
        #             while 0 <= j + d < n:
        #                 j += d

        #                 if nums_cp[j] == 0:
        #                     continue
        #                 else:
        #                     d *= -1
        #                     nums_cp[j] -= 1

        #             if all(k == 0 for k in nums_cp):
        #                 ans += 1

        # return ans

        # Prefix sum and suffix sum solution
        n = len(nums)

        pref = [nums[0]] * n
        suff = [nums[-1]] * n

        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]
            suff[~i] = suff[~(i - 1)] + nums[~i]

        ans = 0
        for i, num in enumerate(nums):
            if num != 0:
                continue
            if pref[i] == suff[i]:
                ans += 2
            elif abs(pref[i] - suff[i]) == 1:
                ans += 1

        return ans
