class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {}

        def dfs(i: int):
            if i >= n:
                return 1

            taken = 0

            # Cases that we can take, because + k or - k is not in taken
            if d.get(nums[i] - k, 0) == 0 and d.get(nums[i] + k, 0) == 0:
                d[nums[i]] = d.get(nums[i], 0) + 1

                # Proceed to next
                taken = dfs(i + 1)

                d[nums[i]] -= 1

            return taken + dfs(i + 1)

        # -1 because non-empty
        return dfs(0) - 1