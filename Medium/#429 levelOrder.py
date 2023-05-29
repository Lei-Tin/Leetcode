"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        ans = []

        level = [root]

        while level != []:
            values = []
            curr_level = []

            for node in level:
                values.append(node.val)
                curr_level.extend(node.children)

            level = curr_level
            ans.append(values)

        return ans
