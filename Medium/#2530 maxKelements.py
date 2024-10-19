class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []

        # MaxHeap
        for num in nums:
            heapq.heappush(pq, -num)

        ans = 0
        for i in range(k):
            val = heapq.heappop(pq)

            if val == -1:
                # Remaining steps
                # Because math ceil is always 1
                # So this adds 1 every single iteration
                return ans + k - i

            ans -= val  # Because val is negative

            replace_val = math.ceil(-val / 3)

            heapq.heappush(pq, -replace_val)

        return ans
