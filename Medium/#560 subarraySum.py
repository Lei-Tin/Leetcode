class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Exceeded runtime brute force solution
        # count = 0
        # prefSums = [0 for _ in range(len(nums))]

        # prefSums[0] = nums[0]
        # for i in range(1, len(nums)):
        #     prefSums[i] = prefSums[i - 1] + nums[i]

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if i == 0:
        #             currSum = prefSums[j]
        #         else:
        #             currSum = prefSums[j] - prefSums[i - 1]

        #         if currSum == k:
        #             count += 1

        # return count

        count = 0
        currSum = 0

        sums = {0: 1}

        for num in nums:
            currSum += num

            # This works because if we once had reached that point where currSum - k is in previous sums
            # Then, we can simply construct subarray by currSum - previousSum = k, so all numbers
            # inbetween this subarray, when added, sums up to k

            # We can construct as many subarrays simply depending on how much previousSums we have

            if currSum - k in sums:
                count += sums[currSum - k]

            sums[currSum] = sums.get(currSum, 0) + 1

        return count
