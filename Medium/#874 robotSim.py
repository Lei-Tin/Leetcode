class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        x, y = 0, 0
        dx, dy = 0, 1  # North

        obs = set()
        for u, v in obstacles:
            obs.add((u, v))

        for query in commands:
            if query == -2:
                dx, dy = -dy, dx
            elif query == -1:
                dx, dy = dy, -dx
            else:
                for i in range(1, query + 1):
                    if (x + dx, y + dy) in obs:
                        break

                    x += dx
                    y += dy

                    ans = max(ans, x ** 2 + y ** 2)

        return ans
