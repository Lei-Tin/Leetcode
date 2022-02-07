# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next

        return prev

        # return self.recursiveReverse(None, head)

#     def recursiveReverse(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
#         """
#         Precondition:
#             - prev is None or prev.next == curr
#             - not (prev is not None and curr is None)
#         """
#         if curr is None:
#             return prev

#         curr.next, prev, curr = prev, curr, curr.next

#         return self.recursiveReverse(prev, curr)

