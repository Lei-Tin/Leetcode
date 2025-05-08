class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        
        for i, (x1, y1) in enumerate(points):
            # Slopes dict here is different depending on which starting point we have
            slopes = {}

            for j, (x2, y2) in enumerate(points[i + 1:]):
                if x2 - x1 == 0:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)

                slopes[slope] = slopes.get(slope, 0) + 1

                ans = max(ans, slopes[slope])

        return ans + 1