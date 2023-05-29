"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        q = deque([node])
        graph = {node.val: Node(node.val, None)}

        while len(q) > 0:
            curr = q.popleft()
            for n in curr.neighbors:
                if n.val not in graph:
                    graph[n.val] = Node(n.val, None)
                    q.append(n)

                graph[curr.val].neighbors.append(graph[n.val])

        return graph[node.val]
