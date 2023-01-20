class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums))]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count:
            buckets[count[num] - 1].append(num)

        j = len(nums) - 1

        ans = []
        while len(ans) < k:
            if len(buckets[j]) > 0:
                ans.append(buckets[j].pop())
            else:
                j -= 1

        return ans
