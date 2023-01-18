class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt_neg = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                cnt_neg += 1

        return 1 if cnt_neg % 2 == 0 else -1
