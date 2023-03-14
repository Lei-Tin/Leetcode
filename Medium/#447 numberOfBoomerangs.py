class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        for p1 in points:
            distDict = {}

            for p2 in points:
                dist = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
                distDict[dist] = 1 + distDict.get(dist, 0)

            for key in distDict:
                ans += (distDict[key] - 1) * distDict[key]

        return ans
