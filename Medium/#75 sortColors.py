class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {i:0 for i in range(3)}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        nums[:count[0]] = [0] * count[0]
        nums[count[0]:count[0] + count[1]] = [1] * count[1]
        nums[count[0] + count[1]:] = [2] * count[2]
