# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Early return if the head doesn't need to be processed
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next

        # I need to keep track of first and even start so that I can link them in the very end
        first = head
        evenstart = head.next

        while odd.next is not None and even.next is not None:
            odd.next = even.next

            odd = odd.next

            even.next = odd.next

            even = even.next

        # Now odd is the list with only the odd nodes
        odd.next = evenstart

        return first
