class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        freqs = [1] + [0 for _ in range(k - 1)]

        currSum = 0

        for num in nums:
            currSum += num

            rem = currSum % k

            ans += freqs[rem]

            freqs[rem] += 1

        return ans
