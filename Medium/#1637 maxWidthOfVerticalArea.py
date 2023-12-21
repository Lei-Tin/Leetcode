class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)

        width = 0

        for i in range(n - 1):
            dist = points[i + 1][0] - points[i][0]

            if dist > width:
                width = dist

        return width
