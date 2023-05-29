class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0

        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                total += num
                count += 1

        if count == 0:
            return 0

        return total // count
