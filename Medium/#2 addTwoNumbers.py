# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans

        carry = 0

        while l1 is not None or l2 is not None:
            add = 0

            if l1 is not None:
                add += l1.val
                l1 = l1.next

            if l2 is not None:
                add += l2.val
                l2 = l2.next

            add += carry

            ans.next = ListNode(add % 10)
            carry = add // 10

            ans = ans.next

        if carry == 1:
            ans.next = ListNode(1)

        return dummy.next
