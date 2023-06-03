class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # BFS Solution
        g = {i: [] for i in range(n)}
        for i in range(len(manager)):
            if manager[i] != -1:
                g[manager[i]].append((i, informTime[i]))

        def bfs(start: int):
            q = deque([(start, informTime[start])])
            cost = 0

            while len(q) > 0:
                n, time = q.popleft()
                cost = max(cost, time)
                for nei, w in g[n]:
                    q.append((nei, time + w))

            return cost

        return bfs(headID)

        # DFS Solution
        # def numOfMinutes(self, n: int, headID: int, manager: List[int],
        #                  informTime: List[int]) -> int:
        #     g = {i: [] for i in range(n)}
        #     for i in range(len(manager)):
        #         if manager[i] != -1:
        #             g[manager[i]].append((i, informTime[i]))
        #
        #     def dfs(i: int) -> int:
        #         ans = informTime[i]
        #         for n, w in g[i]:
        #             ans = max(ans, dfs(n) + informTime[i])
        #
        #         return ans
        #
        #     return dfs(headID)
