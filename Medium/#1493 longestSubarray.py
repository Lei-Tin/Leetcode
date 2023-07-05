class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Solution 1: Sliding window
        i = 0
        j = 0
        ans = 0
        n = len(nums)

        num_zero = 0

        # Let the window to have at most one 0
        while j < n:
            if nums[j] == 0:
                num_zero += 1

            if num_zero == 2:
                while num_zero == 2:
                    if nums[i] == 0:
                        num_zero -= 1
                    i += 1

            ans = max(ans, j - i)
            j += 1

        return ans

        # Solution 2: Count runs
        # prev, curr = 0, 0
        # ans = 0

        # for num in nums:
        #     if num == 1:
        #         curr += 1
        #     else:
        #         ans = max(ans, prev + curr)
        #         prev = curr
        #         curr = 0

        # ans = max(ans, prev + curr)

        # if all(nums[i] == 1 for i in range(len(nums))):
        #     return ans - 1

        # return ans
