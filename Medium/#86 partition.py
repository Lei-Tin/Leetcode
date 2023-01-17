# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Split into 2 partitions
        p1 = ListNode()
        p2 = ListNode()

        p1_head = p1
        p2_head = p2

        curr = head

        while curr is not None:
            if curr.val < x:
                p1.next = curr
                p1 = p1.next
            else:
                p2.next = curr
                p2 = p2.next

            curr = curr.next

        p1.next, p2.next = p2_head.next, None

        return p1_head.next
