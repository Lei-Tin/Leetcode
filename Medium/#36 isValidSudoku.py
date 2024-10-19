class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution 1
        # Optimize storage space
        # Check row
        for row in board:
            for num in row:
                if num.isdigit() and row.count(num) > 1:
                    return False

        # Check column
        for col in range(9):
            seen = {}
            for row in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] not in seen:
                    seen[board[row][col]] = 1
                else:
                    seen[board[row][col]] += 1

            if any(seen[key] > 1 for key in seen):
                return False

        # Check 3 by 3 grid
        vleft = 0
        vright = 3

        hleft = 0
        hright = 3

        while vleft < 9:
            rows = board[vleft:vright]

            hleft = 0
            hright = 3

            while hleft < 9:
                # The current 3 by 3 grid
                grid = rows.copy()

                for row in range(len(rows)):
                    grid[row] = rows[row][hleft:hright]

                seen = {}

                # Check for the 3 by 3 grid
                for row in grid:
                    for col in row:
                        if col == '.':
                            continue

                        if col not in seen:
                            seen[col] = 1
                        else:
                            seen[col] += 1

                if any(seen[key] > 1 for key in seen):
                    return False

                hleft, hright = hright, hright + 3

            vleft, vright = vright, vright + 3

        return True

        # Solution 2
        # Optimize runtime
        # rows = {i: set() for i in range(9)}
        # cols = {i: set() for i in range(9)}
        # grids = {i: set() for i in range(9)}
        #
        # n, m = len(board), len(board[0])
        #
        # for i in range(n):
        #     for j in range(m):
        #         val = board[i][j]
        #         if val == '.':
        #             continue
        #
        #         subgrid_x = i // 3
        #         subgrid_y = j // 3
        #
        #         grid = int(subgrid_x * 3 + subgrid_y)
        #
        #         if val in rows[i] or val in cols[j] or val in grids[grid]:
        #             return False
        #
        #         rows[i].add(val)
        #         cols[j].add(val)
        #         grids[grid].add(val)
        #
        # return True
