class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = deque([])

        directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        time = 0

        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((0, i, j))

        while queue:
            time, i, j = queue.popleft()

            # Set as rotten
            grid[i][j] = 2

            for dx, dy in directions:
                if 0 <= i + dx < n and 0 <= j + dy < m:
                    if grid[i + dx][j + dy] == 1:
                        if (i + dx, j + dy) in visited:
                            continue

                        # Add to queue
                        queue.append((time + 1, i + dx, j + dy))
                        visited.add((i + dx, j + dy))


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return time