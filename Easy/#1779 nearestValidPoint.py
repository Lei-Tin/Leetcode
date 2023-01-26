class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = math.inf
        index = -1
        for i in range(len(points)):
            curr_x, curr_y = points[i]
            if curr_x == x or curr_y == y:
                val = abs(x - curr_x) + abs(y - curr_y)

                if val < dist:
                    index = i
                    dist = val

        return index
