# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        prev = None

        # Traverse till the middle point
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        # Handle the case of odd length list
        if fast is not None:
            slow = slow.next

        while slow is not None:
            if slow.val != prev.val:
                return False

            slow, prev = slow.next, prev.next

        return True

