class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        else:
            answer = []

            for i in range(len(nums)):
                # Pick a number
                curr = nums[i]

                # All the rest
                rest = nums[i + 1:] + nums[:i]

                for j in self.permute(rest):
                    # Here j is a list that is the permutation of rest
                    answer.append([curr] + j)

        return answer

