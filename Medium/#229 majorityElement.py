class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)

        ans = []

        for k, v in d.items():
            if v > len(nums) // 3:
                ans.append(k)

        return ans