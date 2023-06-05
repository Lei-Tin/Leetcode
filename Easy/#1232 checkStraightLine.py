class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # Vertical slope case
        if x1 == x2:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != x1:
                    return False

            return True

        slope = (y2 - y1) / (x2 - x1)
        b = y2 - slope * x2

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]

            if y != slope * x + b:
                return False

        return True

        # # This is always valid because
        # # the question states that we must have at least 2 coordinates
        # x1, y1 = coordinates[0]
        # x2, y2 = coordinates[1]
        #
        # # Case for infinite slope
        # if x1 == x2:
        #     for i in range(2, len(coordinates)):
        #         if coordinates[i][0] != x1:
        #             return False
        #
        #     return True
        #
        # # General case
        # slope = (y2 - y1) / (x2 - x1)
        #
        # # y = mx + b
        # # b = y - mx
        # intercept = y1 - slope * x1
        #
        # for i in range(2, len(coordinates)):
        #     if int(slope * coordinates[i][0] + intercept) != coordinates[i][1]:
        #         return False
        #
        # return True
