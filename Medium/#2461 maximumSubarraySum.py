class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_cnt = Counter(nums[:k])
        curr_sum = sum(nums[:k])

        n = len(nums)

        ans = 0 if len(curr_cnt) < k else curr_sum

        for i in range(k, n):
            curr_sum -= nums[i - k]
            curr_sum += nums[i]

            if nums[i - k] in curr_cnt:
                if curr_cnt[nums[i - k]] - 1 == 0:
                    del curr_cnt[nums[i - k]]
                else:
                    curr_cnt[nums[i - k]] -= 1

            curr_cnt[nums[i]] = curr_cnt.get(nums[i], 0) + 1

            if len(curr_cnt) == k:
                ans = max(ans, curr_sum)

        return ans

