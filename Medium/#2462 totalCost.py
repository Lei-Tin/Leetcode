class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) == 1:
            return costs[0]

        ans = 0

        l = 0
        r = len(costs) - 1

        left_heap = []
        right_heap = []

        i = 0
        while l < r and i < candidates:
            heappush(left_heap, costs[l])
            heappush(right_heap, costs[r])
            l += 1
            r -= 1
            i += 1

        for i in range(k):
            if len(right_heap) == 0 or (len(left_heap) > 0 and left_heap[0] <= right_heap[0]):
                ans += heappop(left_heap)

                if l <= r:
                    heappush(left_heap, costs[l])
                    l += 1

            else:
                ans += heappop(right_heap)

                if l <= r:
                    heappush(right_heap, costs[r])
                    r -= 1

        return ans
