class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # DFS Way
        # g = {}

        # leaf = set()

        # # Reverse all edges
        # for u, v in edges:
        #     # Connect v to u
        #     g.setdefault(v, []).append(u)

        # @cache
        # def dfs(node: int):
        #     # Must be leaf
        #     if node not in g:
        #         leaf.add(node)
        #         return

        #     for next_node in g[node]:
        #         dfs(next_node)

        # # Traverse through all possible paths
        # for i in range(n):
        #     dfs(i)

        # return -1 if len(leaf) > 1 else next(iter(leaf))

        # Faster runtime
        leaf_nodes = {i: 0 for i in range(n)}

        for u, v in edges:
            # Find leaf nodes when the graph is reversed
            # This means that it has no incoming edges to it
            leaf_nodes[v] += 1

        champs = set()

        for i in range(n):
            if leaf_nodes[i] == 0:
                champs.add(i)

        return -1 if len(champs) > 1 else next(iter(champs))
