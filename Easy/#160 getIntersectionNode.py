# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        curr = headA

        while curr is not None:
            visited.add(curr)

            curr = curr.next

        curr2 = headB

        size_of_visited = len(visited)

        while curr2 is not None:
            size_of_visited += 1

            visited.add(curr2)

            if size_of_visited != len(visited):
                return curr2

            curr2 = curr2.next

        return None
