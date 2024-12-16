class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            curr = []
            while num > 0:
                rem = num % 10
                num //= 10

                curr.append(rem)

            ans.extend(curr[::-1])

        return ans
