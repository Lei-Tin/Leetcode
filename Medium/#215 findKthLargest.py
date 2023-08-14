class Solution:
    # O(K) memory and O(NlogK) time
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heappush(pq, n)
            if len(pq) > k:
                heappop(pq)

        return pq[0]

        # Quick select solution, O(n) time and O(1) space
        # pivot = random.choice(nums)

        # smaller = [num for num in nums if num < pivot]
        # equal = [num for num in nums if num == pivot]
        # larger = [num for num in nums if num > pivot]

        # # If we found out that the right hand side, larger has more values than k, then we can just look on the right hand side
        # if len(larger) >= k:
        #     return self.findKthLargest(larger, k)
        # elif k > len(larger) + len(equal):
        #     return self.findKthLargest(smaller, k - len(larger) - len(equal))
        # else:
        #     return equal[0]
