class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n == 0:
            return []

        # Optimized two pointer solution
        ans = []

        i = 0
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start == nums[i]:
                ans.append(f'{start}')
            else:
                ans.append(f'{start}->{nums[i]}')

            i += 1

        return ans

        # Intuitive solution
        # ans = []
        # curr = [nums[0]]

        # for i in range(1, len(nums)):
        #     if curr[-1] + 1 != nums[i]:
        #         if len(curr) == 1:
        #             ans.append(f'{curr[0]}')
        #         else:
        #             ans.append(f'{curr[0]}->{curr[-1]}')
        #         curr = [nums[i]]
        #     else:
        #         curr.append(nums[i])

        # if len(curr) == 1:
        #     ans.append(f'{curr[0]}')
        # else:
        #     ans.append(f'{curr[0]}->{curr[-1]}')

        # return ans
