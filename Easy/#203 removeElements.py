# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Solution 1
        #         new_list = ListNode()
        #         tracker = new_list

        #         curr = head

        #         while curr is not None:
        #             if curr.val != val:
        #                 new_list.next = ListNode(curr.val)
        #                 new_list = new_list.next

        #             curr = curr.next

        #         return tracker.next

        # Solution 2
        tracker = ListNode()
        tracker.next = head

        curr = tracker

        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return tracker.next
