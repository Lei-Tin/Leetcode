"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid[0]) == 0:
            return None

        if self.allTheSame(grid):
            return Node(grid[0][0], True, None, None, None, None)

        else:
            h_center = len(grid) // 2
            v_center = len(grid[0]) // 2

            # Top side
            topLeft = grid[:v_center]
            topRight = topLeft.copy()

            for i in range(len(topLeft)):
                topLeft[i] = topLeft[i][:h_center]
                topRight[i] = topRight[i][h_center:]

            # Bottom side
            bottomLeft = grid[v_center:]
            bottomRight = bottomLeft.copy()

            for i in range(len(bottomLeft)):
                bottomLeft[i] = bottomLeft[i][:h_center]
                bottomRight[i] = bottomRight[i][h_center:]

            return Node(0,
                        False,
                        self.construct(topLeft),
                        self.construct(topRight),
                        self.construct(bottomLeft),
                        self.construct(bottomRight))

    def allTheSame(self, grid: List[List[int]]) -> bool:
        val = grid[0][0]

        for row in grid:
            for value in row:
                if value != val:
                    return False

        return True
