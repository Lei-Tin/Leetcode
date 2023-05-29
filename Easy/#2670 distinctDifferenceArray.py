class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pref = [0 for _ in range(len(nums))]
        suf = [0 for _ in range(len(nums) + 1)]

        front = set()
        for i in range(len(nums)):
            front.add(nums[i])
            pref[i] = len(front)

        back = set()
        for i in range(len(nums) - 1, -1, -1):
            back.add(nums[i])
            suf[i] = len(back)

        ans = []
        for i in range(len(nums)):
            ans.append(pref[i] - suf[i + 1])

        return ans
