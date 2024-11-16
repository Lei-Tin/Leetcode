class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)

        ans = float('inf')

        while l <= r:
            val = (l + r) // 2

            stores_needed = 0

            # Check val
            for q in quantities:
                stores_needed += math.ceil(q / val)

            if stores_needed <= n:
                ans = min(ans, val)
                r = val - 1
            elif stores_needed > n:
                l = val + 1

        return ans
