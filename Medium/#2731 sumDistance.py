# Wasn't able to finish the question in time
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        # Notice that if the robots just "phase through" each other, the result is still the same
        for i in range(len(nums)):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d

        # Utilize a prefix sum
        ans = 0
        pref = 0
        nums.sort()
        for i in range(len(nums)):
            # Notice that the contribution of nums[i] is simply
            # nums[i] - nums[0] + nums[i] - nums[1] + ... + nums[i] - nums[i - 1]
            # This is done by i * nums[i] - pref

            # Then, we will fill in the remaining of nums[i] - nums[i + 1] + ... by
            # When we iterate i to the following iterations, it will automatically give us:
            # nums[i + 2] - nums[0] + ... + nums[i + 2] - nums[i] + nums[i + 2] - nums[i + 1]
            # And this covers exactly the ones we need.
            ans += i * nums[i] % MOD - pref
            pref += nums[i] % MOD

        return ans % MOD

        # # Simulation solution, TLE
        # MOD = 10 ** 9 + 7

        # directions = [1 if char == 'R' else -1 for char in s]

        # for step in range(d):
        #     for i in range(len(nums)):
        #         for j in range(i + 1, len(nums)):
        #             if nums[i] == nums[j]:
        #                 directions[i] *= -1
        #                 directions[j] *= -1

        #     for i in range(len(nums)):
        #         nums[i] += directions[i]

        # ans = 0

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         ans += abs(nums[i] - nums[j]) % MOD

        # return ans % MOD
