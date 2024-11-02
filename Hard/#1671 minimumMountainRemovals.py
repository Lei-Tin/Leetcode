class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        incr = [1] * n
        decr = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    incr[i] = max(incr[i], incr[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    decr[i] = max(decr[i], decr[j] + 1)

        ans = 0

        for i in range(n):
            # Longest increasing + decreasing
            # The rest should be removed

            # This != 1 is used to ensure that there is at least a mountain on the other side
            # So not something like 1 2 3 4 1 5 6
            # You need to remove 5 and 6 instead of 1
            if incr[i] != 1 and decr[i] != 1:
                ans = max(ans, incr[i] + decr[i])

        return n - ans + 1
