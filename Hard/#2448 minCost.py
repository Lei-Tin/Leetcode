class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Prefix and Suffix sum solution
        n = len(nums)

        arr = sorted(zip(nums, cost))

        # Running a prefix cost

        # pre[i] means the cost to turn every single num to the left of nums[i] into nums[i]
        pre = [0 for _ in range(n)]

        curr_cost = arr[0][1]
        for i in range(1, n):
            pre[i] = pre[i - 1] + (arr[i][0] - arr[i - 1][0]) * curr_cost
            curr_cost += arr[i][1]

        # Running a suffix cost
        suf = [0 for _ in range(n)]

        curr_cost = arr[-1][1]
        for i in range(1, n):
            suf[~i] = suf[~(i - 1)] + (arr[~(i - 1)][0] - arr[~i][0]) * curr_cost
            curr_cost += arr[~i][1]

        return min(pre[i] + suf[i] for i in range(n))
