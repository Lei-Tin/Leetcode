class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pref = [0] * (n + 1)

        for l, r in queries:
            pref[l] -= 1
            pref[r + 1] += 1

        for i in range(1, n + 1):
            pref[i] += pref[i - 1]

        for i, num in enumerate(nums):
            if num + pref[i] > 0:
                return False

        return True
