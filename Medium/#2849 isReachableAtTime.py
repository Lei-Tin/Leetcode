class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1

        min_coord = 'x' if abs(fx - sx) < abs(fy - sy) else 'y'

        # Walk diagonally until cannot walk no longer
        min_step = abs(fx - sx) if min_coord == 'x' else abs(fy - sy)

        # Fill in the rest of the distance
        if min_coord == 'x':
            min_step += abs(fy - sy) - abs(fx - sx)
        else:
            min_step += abs(fx - sx) - abs(fy - sy)

        return min_step <= t