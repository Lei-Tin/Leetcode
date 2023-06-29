class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Objective keys count
        objective = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                # If it is a small letter character
                if 97 <= ord(grid[i][j]) <= 122:
                    objective += 1

        visited = set()
        q = deque([(start[0], start[1], '')])

        steps = 0

        while len(q) > 0:
            for _ in range(len(q)):
                # k is the keys we have right now
                x, y, k = q.popleft()

                if len(k) == objective:
                    return steps

                if (x, y, k) in visited:
                    continue

                visited.add((x, y, k))

                for dx, dy in d:
                    new_x = x + dx
                    new_y = y + dy

                    if 0 <= new_x < m and 0 <= new_y < n:
                        # If it is air, we can move
                        if grid[new_x][new_y] in '@.':
                            q.append((new_x, new_y, k))
                        # It is a key
                        elif 97 <= ord(grid[new_x][new_y]) <= 122:
                            if grid[new_x][new_y] not in k:
                                q.append((new_x, new_y, k + chr(ord(grid[new_x][new_y]))))
                            else:
                                q.append((new_x, new_y, k))
                        # It is a lock
                        elif 65 <= ord(grid[new_x][new_y]) <= 90:
                            if chr(ord(grid[new_x][new_y]) + 32) in k:
                                q.append((new_x, new_y, k))

            steps += 1

        return -1
