class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        avg = curr_sum / k

        max_avg = avg
        n = len(nums)
        for i in range(k, n):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]

            max_avg = max(max_avg, curr_sum / k)

        return max_avg