"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        d = {}

        curr = head

        while curr:
            d[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head

        while curr:
            new = d[curr]

            if curr.next:
                new.next = d[curr.next]

            if curr.random:
                new.random = d[curr.random]

            curr = curr.next

        return d[head]
