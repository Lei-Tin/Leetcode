class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = {i: [i + 1] if i != n - 1 else [] for i in range(n)}

        ans = []

        for u, v in queries:
            g[u].append(v)

            dq = Deque([(0, 0)])

            dist = [float('inf')] * n
            dist[0] = 0

            while dq:
                curr, s = dq.popleft()

                # If we have some other way to reach here with lesser travels, we give up this path
                if dist[curr] < s:
                    continue

                dist[curr] = s

                if curr == n - 1:
                    ans.append(s)
                    break

                else:
                    for neighbor in g[curr]:
                        dq.append((neighbor, s + 1))

        return ans
