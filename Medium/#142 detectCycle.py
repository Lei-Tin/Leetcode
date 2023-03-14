# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        slow_count = 0
        fast_count = 0

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            slow_count += 1
            fast_count += 2

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        while head != slow:
            head, slow = head.next, slow.next

        return slow
