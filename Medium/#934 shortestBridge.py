class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        v = set()
        q = deque()

        for r, c in product(range(n), range(n)):
            # Change all 1s to 2 in the first island
            if grid[r][c] == 1:
                self.change(grid, v, q, r, c, n)
                break

        while len(q) > 0:
            r, c, s = q.popleft()
            if grid[r][c] == 1:
                return s - 1

            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if not (0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in v):
                    continue

                v.add((r + dr, c + dc))
                q.append((r + dr, c + dc, s + 1))

        return 0

    def change(self, grid: List[List[int]], v: set, q: deque, r: int, c: int, n: int) -> None:
        if not (0 <= r < n and 0 <= c < n and grid[r][c] == 1):
            return

        grid[r][c] = 2
        v.add((r, c))
        q.append((r, c, 0))

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            self.change(grid, v, q, r + dr, c + dc, n)
