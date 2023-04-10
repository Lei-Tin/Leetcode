class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sol 2
        vals = {}
        for i in range(len(nums)):
            vals[i] = nums[i]

        for i in range(len(nums)):
            nums[i] = vals[(i - k) % len(nums)]

        # # n is the copy of nums
        # n = nums.copy()
        #
        # for i in range(len(nums)):
        #     nums[i] = n[(i - k) % len(nums)]
