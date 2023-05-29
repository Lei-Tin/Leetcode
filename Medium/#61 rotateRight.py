# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        if k == 0:
            return head

        length = 1
        curr = head
        while curr.next is not None:
            length += 1
            curr = curr.next

        # Making it a circular linked list
        curr.next = head

        rot = length - (k % length)

        curr = head
        for _ in range(rot - 1):
            curr = curr.next

        ret, curr.next = curr.next, None

        return ret
