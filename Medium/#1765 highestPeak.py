class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        water_locations = []
        visited = set()

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    water_locations.append((i, j, 0))
                    visited.add((i, j))

        queue = Deque(water_locations)

        dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        while queue:
            x, y, height = queue.popleft()

            isWater[x][y] = height

            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    # Valid location
                    if (new_x, new_y) not in visited:
                        queue.append((new_x, new_y, height + 1))
                        visited.add((new_x, new_y))

        return isWater