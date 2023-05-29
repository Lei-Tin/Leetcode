class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Solution 1
        # We can just find all the nodes that doesn't have any nodes pointing to it
        ends = set()
        for _, end in edges:
            if end not in ends:
                ends.add(end)

        return list(set(i for i in range(n)) - ends)

        # Solution 2
        # Return the nodes that have no nodes pointing to it
        # can_reach = {v for _, v in edges}
        # return [i for i in range(n) if i not in can_reach]
