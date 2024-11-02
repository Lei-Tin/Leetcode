class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        d = {}

        max_val = 0
        for r in range(h):
            max_val = max(max_val, self.search(grid, r, 0, h, w, d))

        return max_val

    def search(self, grid: List[List[int]], r: int, c: int, h: int, w: int, d: dict) -> int:
        if not (0 <= r < h and 0 <= c < w):
            return 0

        if (r, c) in d:
            return d[(r, c)]

        max_move = 0
        for dr, dc in ((-1, 1), (0, 1), (1, 1)):
            if 0 <= r + dr < h and 0 <= c + dc < w:
                if grid[r + dr][c + dc] > grid[r][c]:
                    max_move = max(max_move, 1 + self.search(grid, r + dr, c + dc, h, w, d))

        d[(r, c)] = max_move
        return max_move
