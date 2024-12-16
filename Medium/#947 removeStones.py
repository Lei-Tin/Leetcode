class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        clusters = 0

        row = {}
        col = {}

        for x, y in stones:
            row.setdefault(x, []).append(y)
            col.setdefault(y, []).append(x)

        visited = set()
        not_visited = set(tuple(e) for e in stones)

        def dfs(x, y):
            visited.add((x, y))
            not_visited.remove((x, y))

            for neighbor in row[x]:
                if (x, neighbor) not in visited:
                    dfs(x, neighbor)

            for neighbor in col[y]:
                if (neighbor, y) not in visited:
                    dfs(neighbor, y)

        while not_visited:
            clusters += 1
            x, y = next(iter(not_visited))
            dfs(x, y)

        return len(stones) - clusters
