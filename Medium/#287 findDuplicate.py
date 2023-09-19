class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Sorting solution
        # nums.sort()
        # n = len(nums)
        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]

        # Using Floyd's Tortoise and Hare (Cycle Detection)
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
