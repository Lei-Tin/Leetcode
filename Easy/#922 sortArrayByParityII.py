class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # In place solution
        even = 0
        odd = 1

        while even < len(nums) and odd < len(nums):
            if nums[even] % 2 != 0 and nums[odd] % 2 == 0:
                # So we are at an even index with odd number
                # If we are at odd index with even number
                nums[even], nums[odd] = nums[odd], nums[even]

                even += 2
                odd += 2

            elif nums[even] % 2 != 0 and nums[odd] % 2 != 0:
                odd += 2
            elif nums[even] % 2 == 0 and nums[odd] % 2 == 0:
                even += 2
            else:
                # All of them are in the right place
                odd += 2
                even += 2

        return nums

        # ans = [0 for _ in range(len(nums))]

        # even = 0
        # odd = 1

        # for num in nums:
        #     if num % 2 == 0:
        #         ans[even] = num
        #         even += 2
        #     else:
        #         ans[odd] = num
        #         odd += 2

        # return ans
