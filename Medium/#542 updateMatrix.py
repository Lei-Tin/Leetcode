class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < m:
                    if mat[new_x][new_y] == -1:
                        mat[new_x][new_y] = mat[x][y] + 1
                        q.append((new_x, new_y))

        return mat
