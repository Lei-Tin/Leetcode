class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int,
                    by2: int) -> int:
        a1 = (ax2 - ax1) * (ay2 - ay1)
        a2 = (bx2 - bx1) * (by2 - by1)

        # Calculating intersection area
        overlap_x = 0
        overlap_y = 0

        # X Left and X Right
        max_xl = max(ax1, bx1)
        min_xr = min(ax2, bx2)

        if max_xl < min_xr:
            overlap_x = min_xr - max_xl

        # Y Bottom and Y Upper
        max_yb = max(ay1, by1)
        min_yu = min(ay2, by2)

        if max_yb < min_yu:
            overlap_y = min_yu - max_yb

        return a1 + a2 - (overlap_x * overlap_y)


