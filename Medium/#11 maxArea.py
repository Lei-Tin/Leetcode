class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)

        l, r = 0, n - 1

        while l < r:
            width = r - l

            ans = max(ans, width * min(height[l], height[r]))

            # Move the shorter one
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans
