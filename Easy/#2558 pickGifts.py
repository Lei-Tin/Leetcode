class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []
        for item in gifts:
            heapq.heappush(pq, -item)

        for i in range(k):
            if len(pq) > 0 and pq[0] == -1:
                break

            max_val = -heapq.heappop(pq)
            heapq.heappush(pq, -math.floor(math.sqrt(max_val)))

        return -sum(pq)
