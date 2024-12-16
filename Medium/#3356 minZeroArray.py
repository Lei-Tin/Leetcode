class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def is_possible(k):
            pref = [0] * (n + 1)

            for l, r , val in queries[:k]:
                pref[l] -= val
                pref[r + 1] += val

            for i in range(1, n + 1):
                pref[i] += pref[i - 1]

            for i in range(n):
                if nums[i] + pref[i] > 0:
                    return False
            return True

        ans = None

        low = 0
        high = len(queries) + 1

        while low < high:
            mid = (low + high) // 2

            if is_possible(mid):
                ans = mid
                high = mid
            else:
                low = mid + 1

        return ans if ans != None else -1
