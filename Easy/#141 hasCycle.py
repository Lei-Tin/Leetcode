# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr = head

        while curr is not None and curr not in visited:
            visited.append(curr)
            curr = curr.next

        if curr in visited:
            return True

        return False
