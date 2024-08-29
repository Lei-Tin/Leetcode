class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        g = {i: [] for i in range(n)}
        for i, (u, v) in enumerate(edges):
            g[u].append((v, succProb[i]))
            g[v].append((u, succProb[i]))

        # TLE Backtrack solution
        # visited = {start_node}

        # # backtrack
        # def explore(curr, curr_prob):
        #     if curr == end_node:
        #         return curr_prob

        #     max_ans = 0

        #     neighbors = g[curr]
        #     for neighbor, cost in neighbors:
        #         if neighbor not in visited:
        #             visited.add(neighbor)
        #             max_ans = max(max_ans, explore(neighbor, curr_prob * cost))
        #             visited.remove(neighbor)

        #     return max_ans

        # return explore(start_node, 1)

        # dijkstra solution
        pq = []
        heapq.heappush(pq, (-1, start_node))

        reach = [0] * n

        reach[start_node] = 1

        while len(pq) > 0:
            cost, curr_node = heapq.heappop(pq)

            cost = -cost

            if curr_node == end_node:
                return cost

            for neighbor, prob in g[curr_node]:
                # Update value to reach if it is more likely (higher probability)
                new_cost = prob * cost

                if new_cost > reach[neighbor]:
                    reach[neighbor] = new_cost
                    heapq.heappush(pq, (-new_cost, neighbor))

        return 0

