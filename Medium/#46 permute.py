class Solution:

    # Bitmask solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        # Since 1 <= nums.length <= 6, we can use bitmask
        largest_mask = (1 << n) - 1

        def solve(curr: List[int], mask: int) -> None:
            if mask == largest_mask:
                ans.append(curr)
                return

            for i in range(n):
                # If it is not used in the current bit, then use it
                if 1 << i & mask == 0:
                    new_mask = mask + (1 << i)
                    new_curr = curr.copy()
                    new_curr.append(nums[i])
                    solve(new_curr, new_mask)

        solve([], 0)

        return ans
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 1:
    #         return [nums]
    #
    #     else:
    #         answer = []
    #
    #         for i in range(len(nums)):
    #             # Pick a number
    #             curr = nums[i]
    #
    #             # All the rest
    #             rest = nums[i + 1:] + nums[:i]
    #
    #             for j in self.permute(rest):
    #                 # Here j is a list that is the permutation of rest
    #                 answer.append([curr] + j)
    #
    #     return answer

