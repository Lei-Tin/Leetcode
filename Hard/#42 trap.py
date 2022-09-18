class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        maxLeft, maxRight = height[0], height[-1]
        left, right = 1, len(height) - 2

        while left <= right:
            if maxLeft <= maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]

                else:
                    ans += maxLeft - height[left]

                left += 1

            else:
                if height[right] > maxRight:
                    maxRight = height[right]

                else:
                    ans += maxRight - height[right]

                right -= 1

        return ans
