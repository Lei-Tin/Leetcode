class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k

        for num in nums:
            heappush(self.pq, num)
            if len(self.pq) > k:
                heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heappush(self.pq, val)
            return self.pq[0]

        elif val <= self.pq[0]:
            return self.pq[0]
        else:
            heappush(self.pq, val)
            if len(self.pq) > self.k:
                heappop(self.pq)
            return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
