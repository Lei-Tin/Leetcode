# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        second = head

        for i in range(k - 1):
            first = first.next

        curr = first
        while curr.next is not None:
            second = second.next
            curr = curr.next

        first.val, second.val = second.val, first.val

        return head
