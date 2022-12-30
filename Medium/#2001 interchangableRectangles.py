class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        ratios = {}

        for rect in rectangles:
            ratio = rect[0] / rect[1]
            ratios[ratio] = ratios.get(ratio, 0) + 1

        for ratio in ratios:
            ans += (ratios[ratio] * (ratios[ratio] - 1))

        return ans // 2
