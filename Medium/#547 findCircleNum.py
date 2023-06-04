class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # If isConnected[orig][nei] == 1, then they are neighbors

        def dfs(i: int, visited: set):
            if i in visited:
                return

            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    dfs(j, visited)

        all_visited = set()
        cnt = 0

        for i in range(n):
            if i not in all_visited:
                v = set()
                dfs(i, v)
                all_visited = all_visited.union(v)
                cnt += 1

        return cnt
