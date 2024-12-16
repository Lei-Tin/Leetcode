class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]],
                       walls: List[List[int]]) -> int:
        s = set()

        # 0 for empty
        # 1 for guard
        # 2 for wall
        mat = [[0 for _ in range(n)] for _ in range(m)]

        for x, y in walls:
            mat[x][y] = 2

        for x, y in guards:
            mat[x][y] = 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in guards:
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                while 0 <= next_x < m and 0 <= next_y < n:
                    if mat[next_x][next_y] in {1, 2}:
                        break

                    s.add((next_x, next_y))

                    next_x, next_y = next_x + dx, next_y + dy

        return m * n - len(s) - len(walls) - len(guards)
