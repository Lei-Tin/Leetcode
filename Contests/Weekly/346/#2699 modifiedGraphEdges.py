class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int,
                           target: int) -> List[List[int]]:
        g = {i: [] for i in range(n)}
        weights = {}
        for u, v, w in edges:
            g[u].append(v)
            g[v].append(u)

            weights[(u, v)] = w
            weights[(v, u)] = w

        res_neg = []
        res_skip = []
        self.search(source, destination, [source], g, weights, res_neg, False)
        self.search(source, destination, [source], g, weights, res_skip, True)

        min_cost_neg = 10 ** 9
        min_cost_skip = 10 ** 9

        for path in res_skip:
            cost = 0
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                cost += weights[(u, v)]

            min_cost_skip = min(min_cost_skip, cost)

        min_path = []

        for path in res_neg:
            cost = 0
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]

                if weights[(u, v)] == -1:
                    cost += 1
                else:
                    cost += weights[(u, v)]
            if cost < min_cost_neg:
                min_cost_neg = min(min_cost_neg, cost)
                min_path = path

        change = []
        for i in range(len(min_path) - 1):
            u, v = min_path[i], min_path[i + 1]

            if weights[(u, v)] == -1:
                change.append((u, v))

        if min_cost_skip < target:
            return []

        if min_cost_skip > target and min_cost_neg > target:
            return []

        if min_cost_skip < min_cost_neg and min_cost_skip == target:
            return [[u, v, w] if w != -1 else [u, v, 1] for u, v, w in edges]

        if len(change) == 0 and min_cost_neg < target:
            return []

        target = target - min_cost_neg + len(change)

        u, v = change[0]
        weights[(u, v)] = target - len(change) + 1
        weights[(v, u)] = target - len(change) + 1

        for i in range(1, len(change)):
            u, v = change[i]

            weights[(u, v)] = 1
            weights[(v, u)] = 1

        return [[u, v, weights[(u, v)]] if weights[(u, v)] != -1 else [u, v, 1] for u, v, w in
                edges]

    def search(self, start: int, end: int, path: list, graph: dict, weights: dict, res: List,
               skip: bool) -> None:
        if len(path) >= 2 and path[-1] == end:
            res.append(path)

        for n in graph[path[-1]]:
            if n not in path:
                if skip and weights[(path[-1], n)] == -1:
                    continue
                else:
                    self.search(start, end, path + [n], graph, weights, res, skip)

        return
