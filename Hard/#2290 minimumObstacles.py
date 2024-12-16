class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        min_cost = {(i, j): float('inf') for i in range(n) for j in range(m)}
        min_cost[(0, 0)] = 0

        # Each item in deque is x, y, score
        dq = Deque([(0, 0, 0)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            x, y, cost = dq.popleft()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    if min_cost[(new_x, new_y)] == float('inf'):
                        min_cost[(new_x, new_y)] = cost + grid[new_x][new_y]

                        if grid[new_x][new_y] == 0:
                            dq.appendleft((new_x, new_y, cost + grid[new_x][new_y]))
                        else:
                            dq.append((new_x, new_y, cost + grid[new_x][new_y]))

        return min_cost[(n - 1, m - 1)]
