# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr is not None:
            curr = curr.next
            length += 1

        prev, curr = None, head
        for i in range(length - n):
            prev, curr = curr, curr.next

        if length == 1:
            # If we want to remove a list with only 1 item
            return None

        elif n == length:
            # We want to remove the first item
            return curr.next

        else:
            prev.next = curr.next

        return head
