class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # We can just find all the nodes that doesn't have any nodes pointing to it
        ends = set()
        for _, end in edges:
            if end not in ends:
                ends.add(end)

        return list(set(i for i in range(n)) - ends)
