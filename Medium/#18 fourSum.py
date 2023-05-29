class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        seen = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # Check if complement of the target with these three numbers is in seen
                    comple = target - nums[i] - nums[j] - nums[k]

                    if comple in seen:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], comple])))

            seen.add(nums[i])

        return list(ans)
