class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pq = []
        curr_sum = 0
        ans = 0

        for s, e in sorted(zip(speed, efficiency), reverse=True, key=lambda x: x[1]):
            heappush(pq, s)
            curr_sum += s

            if len(pq) > k:
                curr_sum -= heappop(pq)

            ans = max(ans, curr_sum * e)

        return ans % (10 ** 9 + 7)
