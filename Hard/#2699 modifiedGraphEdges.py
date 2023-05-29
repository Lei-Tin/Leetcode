class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int,
                           target: int) -> List[List[int]]:
        g = {i: [] for i in range(n)}
        weights = {}
        for u, v, w in edges:
            g[u].append(v)
            g[v].append(u)

            weights[(min(u, v), max(u, v))] = w

        # Check dijkstra ignoring negatives
        dist_rev, parent_rev = self.dijkstra(destination, g, weights.copy(), True)
        # If there exists a path from source to destination that is lesser than target, return []
        if dist_rev.get(source, inf) < target:
            return []

        # Saving the reverse for later use

        dist, parent = self.dijkstra(source, g, weights.copy(), False)
        # This means the shortest distance from source to destination with weights being 1 is
        if dist.get(destination, inf) > target:
            return []

        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])

        path = path[::-1]
        walked = 0

        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]

            if weights[(min(u, v), max(u, v))] == -1:
                weights[(min(u, v), max(u, v))] = max(target - dist_rev.get(v, inf) - walked, 1)

            walked += weights[(min(u, v), max(u, v))]

        for u, v in weights:
            if weights[(u, v)] == -1:
                weights[(u, v)] = target + 1

        return [[u, v, weights[(u, v)]] for u, v in weights]

    def dijkstra(self, source: int, g: dict, w: dict, skip: bool) -> Tuple[dict, dict]:
        pq = []
        heappush(pq, (0, source))

        dist = {}
        parent = {}

        dist[source] = 0
        parent[source] = None

        while len(pq) > 0:
            d, n = heappop(pq)
            if d > dist.get(n, inf):
                # If the distance from curr to n is lesser than recorded
                # minimum, we don't take this path
                continue

            for neighbor in g[n]:
                if w[(min(n, neighbor), max(n, neighbor))] == -1:
                    if skip:
                        continue
                    else:
                        w[(min(n, neighbor), max(n, neighbor))] = 1

                new_dist = d + w[(min(n, neighbor), max(n, neighbor))]

                if new_dist < dist.get(neighbor, inf):
                    dist[neighbor] = new_dist
                    parent[neighbor] = n
                    heappush(pq, (new_dist, neighbor))

        return dist, parent
