def dfs(g: dict, cur: int, visited: set):
    if cur in visited:
        return

    visited.add(cur)

    for neighbor in g[cur]:
        dfs(g, neighbor, visited)
