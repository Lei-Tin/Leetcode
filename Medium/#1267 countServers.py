class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        r = {i: 0 for i in range(n)}
        c = {i: 0 for i in range(m)}

        computer_locations = set()

        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    r[x] += 1
                    c[y] += 1

                    computer_locations.add((x, y))

        ans = 0

        for x, y in computer_locations:
            # Check removing myself, if there's still anyone
            # Same row
            row = r[x] > 1
            col = c[y] > 1
            
            ans += int(row or col)

        return ans
            

        