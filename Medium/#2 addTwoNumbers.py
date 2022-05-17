# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        ans = dummy

        curr1, curr2 = l1, l2

        # This is the number to add to the next digit
        add = 0

        while curr1 is not None or curr2 is not None:
            val1 = curr1.val if curr1 is not None else 0
            val2 = curr2.val if curr2 is not None else 0

            # We add the digits together and add the carry-over term from the last digit
            summation = val1 + val2 + add

            curr_digit = summation % 10
            add = summation // 10

            ans.next = ListNode(curr_digit)

            ans = ans.next

            curr1 = curr1.next if curr1 is not None else None
            curr2 = curr2.next if curr2 is not None else None

        if add == 1:
            ans.next = ListNode(1)

        return dummy.next
