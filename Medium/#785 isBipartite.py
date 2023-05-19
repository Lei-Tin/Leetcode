# Solution 1: Not using a flag
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        visited = set()

        for i in range(len(graph)):
            if i not in visited:
                if self.search(i, color, graph, visited):
                    return False

        return True

    def search(self, start: int, color: list, graph: List[List[int]], visited: set) -> bool:
        visited.add(start)

        for n in graph[start]:
            if n not in visited:
                color[n] = not color[start]

                if self.search(n, color, graph, visited):
                    return True
            else:
                if color[n] == color[start]:
                    return True

        return False

# Solution 2: Using a flag
# class Solution:
#     def __init__(self):
#         self.f = True
#
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         color = [0 for _ in range(len(graph))]
#         visited = set()
#
#         for i in range(len(graph)):
#             if i not in visited:
#                 self.search(i, color, graph, visited)
#
#         return self.f
#
#     def search(self, start: int, color: list, graph: List[List[int]], visited: set) -> None:
#         visited.add(start)
#
#         for n in graph[start]:
#             if n not in visited:
#                 color[n] = not color[start]
#
#                 self.search(n, color, graph, visited)
#
#             if color[n] == color[start]:
#                 self.f = False
