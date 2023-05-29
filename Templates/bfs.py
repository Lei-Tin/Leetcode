def bfs(g: dict, start: int):
    visited = set()
    visited.add(start)
    q = deque([start])
    
    while len(q) > 0:
        node = q.popleft()
        for neighbor in g[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
