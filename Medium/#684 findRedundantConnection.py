class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]  # Each node has itself as parent initially

        def find_root(x):
            while parents[x] != x:
                x = parents[x]

            return x

        for u, v in edges:
            ru = find_root(u)
            rv = find_root(v)
            if ru == rv:
                return [u, v]

            else:
                # Join the two components
                # Point v to u
                parents[ru] = rv