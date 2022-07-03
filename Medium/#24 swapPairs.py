# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #         # Iterative solution

    #         # Here we want the header to be the item before anything
    #         # So that we can use the items at index 1 to be the new header
    #         header = ListNode(-1)
    #         header.next = head

    #         curr = header

    #         # If we don't have at least 2 more nodes for us to swap
    #         while curr.next is not None and curr.next.next is not None:
    #             odd = curr.next
    #             even = curr.next.next

    #             curr.next, odd.next, even.next = even, even.next, odd

    #             # Advance 2 units
    #             curr = curr.next.next

    #         return header.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution

        # If we are in the last 1 node or None, we don't swap
        if head is None or head.next is None:
            return head

        header = head.next.next

        head, head.next = head.next, head

        head.next.next = self.swapPairs(header)

        return head
