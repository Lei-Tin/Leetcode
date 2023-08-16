class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = []

        ans = []

        for i in range(k):
            # Placing the value in index 0 so the max heap is based of that
            heappush(pq, (-nums[i], i))

        ans.append(-pq[0][0])

        for i in range(k, n):
            heappush(pq, (-nums[i], i))

            # If the current largest is still outside of the current window, we remove
            while len(pq) > 0 and pq[0][1] + k <= i:
                heappop(pq)

            ans.append(-pq[0][0])

        return ans
