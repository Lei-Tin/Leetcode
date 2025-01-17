class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # n = len(nums)

        # pref = [0 for _ in range(n + 1)]
        # suff = [0 for _ in range(n + 1)]

        # for i in range(1, n + 1):
        #     pref[i] = pref[i - 1] + nums[i - 1]
        #     suff[~i] = suff[~(i - 1)] + nums[~(i - 1)]

        # ans = 0

        # for i in range(1, n):
        #     if pref[i] >= suff[i]:
        #         ans += 1

        # return ans

        # Optimized solution
        n = len(nums)
        total = sum(nums)

        ans = 0

        curr = 0
        for num in nums[:-1]:
            curr += num

            if curr >= total - curr:
                ans += 1

        return ans