class NumArray:

    def __init__(self, nums: List[int]):
        self.prefSums = [0 for _ in range(len(nums))]

        self.prefSums[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefSums[i] = self.prefSums[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefSums[right]

        return self.prefSums[right] - self.prefSums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
