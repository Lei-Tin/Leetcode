class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]

        front = 1
        end = 1

        for i in range(len(nums)):
            # Assigning like this works because at first
            # ans[0] only has 1, but the end carries all the multiplied values back to ans[0]
            # Similarly, the value in the end only initially has 1, but front carries all the multiplied value there
            # Technically, all the values at any index initially only has 1, which is the same as removing their values
            ans[i] *= front
            ans[-i - 1] *= end

            front *= nums[i]
            end *= nums[-i - 1]

        return ans
