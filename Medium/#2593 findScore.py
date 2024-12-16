class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Heap solution
        # pq = []

        # for i, num in enumerate(nums):
        #     heapq.heappush(pq, (num, i))

        # marked = set()
        # ans = 0

        # while pq:
        #     val, i = heapq.heappop(pq)
        #     if i in marked:
        #         continue

        #     marked.add(i)
        #     marked.add(i - 1)
        #     marked.add(i + 1)

        #     ans += val

        # return ans

        # Monotonic stack solution
        stack = []
        ans = 0

        for num in nums:
            if not stack or num < stack[-1]:
                stack.append(num)
            else:
                while stack:
                    ans += stack.pop()
                    if stack:
                        stack.pop()  # Double pop to ensure the cliff leading to the local min is marked as well

        # Deal with remaining monotonically decreasing values in the stack
        while stack:
            ans += stack.pop()
            if stack:
                stack.pop()

        return ans
