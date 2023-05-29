class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Generate the n by n matrix
        ans = [[0 for _ in range(n)] for _ in range(n)]

        x, y = 0, 0
        dx, dy = 1, 0

        # Try to walk along in the spiral path
        for i in range(n * n):
            # Set the number
            ans[y][x] = i + 1

            # If next step is still within boundaries and is unfilled, then we walk
            if 0 <= x + dx < n and 0 <= y + dy < n and ans[y + dy][x + dx] == 0:
                x += dx
                y += dy
            else:
                # We want to turn when it exceeds n OR if we meet a number in front
                # Execute turn right
                # 1, 0 -> 0, 1
                # 0, 1 -> -1, 0
                # -1, 0 -> 0, -1
                # 0, -1 -> 1, 0

                # This generalizes to dx, dy = -dy, dx
                dx, dy = -dy, dx
                x += dx
                y += dy

        return ans
