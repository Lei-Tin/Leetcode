class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        for x, y, r in queries:
            pts = 0
            r2 = r ** 2
            for xloc, yloc in points:
                if (xloc - x) ** 2 + (yloc - y) ** 2 <= r2:
                    pts += 1

            ans.append(pts)

        return ans
