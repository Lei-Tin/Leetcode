class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:
                for j in range(k):
                    if i + j + 1 < len(nums) and nums[i + j + 1] == 1:
                        return False

        return True
