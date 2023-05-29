class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = []
        ans = 0
        curr_sum = 0

        for n1, n2 in sorted(zip(nums1, nums2), reverse=True, key=lambda x: x[1]):
            heappush(pq, n1)
            curr_sum += n1

            if len(pq) == k:
                ans = max(ans, curr_sum * n2)
                curr_sum -= heappop(pq)

        return ans
