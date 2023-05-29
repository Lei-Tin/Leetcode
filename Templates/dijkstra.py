def shortestPath(self, node1: int, node2: int) -> int:
    # Distance recorded to reach each node
    dist = [inf for _ in range(len(self.g))]
    dist[node1] = 0
    pq = [(0, node1)]

    while len(pq) > 0:
        d, n = heappop(pq)
        if n == node2:
            return d

        if d > dist[n]:
            # We don't take this path
            continue

        for neighbor, w in self.g[n]:

            if d + w < dist[neighbor]:
                dist[neighbor] = d + w
                heappush(pq, (d + w, neighbor))

    return -1
