class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #         left_ptr = right_ptr = 0

        #         while left_ptr < len(nums):
        #             if nums[left_ptr] == 0:
        #                 right_ptr = left_ptr
        #                 while nums[right_ptr] == 0 and right_ptr < len(nums) - 1:
        #                     right_ptr += 1

        #                 nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]

        #             left_ptr += 1

        # Version 2
        num_zeroes = 0
        length = len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeroes += 1

        for i in range(num_zeroes):
            nums.remove(0)
            nums.insert(length, 0)

