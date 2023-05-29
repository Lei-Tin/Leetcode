# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0
        #
        # curr = head
        #
        # while curr is not None:
        #     curr = curr.next
        #     length += 1
        #
        # index = length // 2
        #
        # curr = head
        #
        # for i in range(index):
        #     curr = curr.next
        #
        # return curr

        # Version 2

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
