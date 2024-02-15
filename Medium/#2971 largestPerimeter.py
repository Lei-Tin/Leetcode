class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        pref = []

        nums.sort()
        curr_sum = 0

        for num in nums:
            curr_sum += num
            pref.append(curr_sum)

        for i in range(n - 1, -1, -1):
            if pref[i] - nums[i] > nums[i]:
                return pref[i]

        return -1
