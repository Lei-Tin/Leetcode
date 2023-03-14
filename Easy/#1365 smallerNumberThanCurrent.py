class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numDict = {}

        for num in nums:
            numDict[num] = 1 + numDict.get(num, 0)

        ans = []

        for i in range(len(nums)):
            mySum = 0

            for j in range(nums[i]):
                mySum += numDict.get(j, 0)

            ans.append(mySum)

        return ans
