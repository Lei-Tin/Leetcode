class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]

        left[0] = nums[0]
        right[-1] = nums[-1]

        # Find the minimum left from left till right
        for i in range(1, len(nums)):
            left[i] = min(left[i - 1], nums[i])

        # Find the maximum right from right till left
        for i in range(len(nums) - 2, -1, -1):
            right[i] = max(right[i + 1], nums[i])

        # Check if we have any satisfying sequence
        for i in range(len(nums)):
            if left[i] < nums[i] < right[i]:
                return True

        return False
