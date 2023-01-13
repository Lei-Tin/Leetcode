# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head

        # Get the middle node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # From that node onwards, I want to reverse the second half, that begins with slow.next

        prev, curr = None, slow.next

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Removing the left end, otherwise it creates a loop
        slow.next = None

        # Now prev is the reversed part

        curr1, curr2 = head, prev
        while curr1 and curr2:
            curr1.next, curr1, curr2.next, curr2 = curr2, curr1.next, curr1.next, curr2.next
