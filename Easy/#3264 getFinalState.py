class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))

        for i in range(k):
            val, idx = heapq.heappop(pq)

            heapq.heappush(pq, (val * multiplier, idx))

        for x, i in pq:
            nums[i] = x

        return nums
